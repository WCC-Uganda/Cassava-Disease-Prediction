"""
Streamlit Application: Cassava Leaf Disease Diagnostic & Management System
Developed for War Child Canada - West Nile Cassava Monitoring & School Feeding Project
"""

import os
import sys

# Set legacy Keras mode for compatibility with models saved in Keras 2
os.environ['TF_USE_LEGACY_KERAS'] = '1'

# Ensure app directory is on Python path
APP_DIR = os.path.dirname(os.path.abspath(__file__))
if APP_DIR not in sys.path:
    sys.path.insert(0, APP_DIR)

import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np

# Optional Plotly for Interactive Visualization
try:
    import plotly.express as px
    import plotly.graph_objects as go
    HAS_PLOTLY = True
except ImportError:
    HAS_PLOTLY = False

from utils.disease_data import CLASS_SHORT, FULL_NAMES, DISEASE_DETAILS
from utils.model_loader import load_cassava_model, predict_disease

# Helper functions for Streamlit rendering compatibility
def render_image(image, caption=None):
    try:
        st.image(image, caption=caption, use_container_width=True)
    except TypeError:
        st.image(image, caption=caption)

def render_dataframe(df):
    try:
        st.dataframe(df, hide_index=True, width='stretch')
    except TypeError:
        try:
            st.dataframe(df, hide_index=True, use_container_width=True)
        except Exception:
            st.dataframe(df, hide_index=True)

def render_plotly(fig):
    try:
        st.plotly_chart(fig, width='stretch')
    except TypeError:
        try:
            st.plotly_chart(fig, use_container_width=True)
        except Exception:
            st.plotly_chart(fig)

def render_result_metric(label, value):
    st.markdown(
        f"""
        <div class="result-metric-card">
            <div class="result-metric-label">{label}</div>
            <div class="result-metric-value">{value}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Page Configuration
st.set_page_config(
    page_title="Cassava Disease Prediction - War Child Canada",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.2rem;
        font-weight: 700;
        color: #1E3A8A;
        margin-bottom: 0px;
    }
    .sub-header {
        font-size: 1.05rem;
        color: #4B5563;
        margin-bottom: 20px;
    }
    .metric-card {
        background-color: #F3F4F6;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #2563EB;
    }
    .result-metric-card {
        background-color: #F8FAFC;
        border: 1px solid #D1D5DB;
        border-radius: 10px;
        padding: 12px 14px;
        min-height: 88px;
    }
    .result-metric-label {
        font-size: 0.85rem;
        font-weight: 600;
        color: #374151;
        margin-bottom: 6px;
    }
    .result-metric-value {
        font-size: 1rem;
        font-weight: 700;
        color: #111827;
        line-height: 1.3;
        white-space: normal;
        overflow-wrap: anywhere;
        word-break: break-word;
    }
    .treatment-box {
        background-color: #F0FDF4;
        border: 1px solid #BBF7D0;
        border-radius: 8px;
        padding: 15px;
        margin-top: 10px;
    }
    @media (max-width: 768px) {
        .main-header {
            font-size: 1.6rem;
        }
        .sub-header {
            font-size: 0.95rem;
        }
        .result-metric-card {
            min-height: 78px;
            padding: 10px 12px;
        }
        .result-metric-label {
            font-size: 0.78rem;
        }
        .result-metric-value {
            font-size: 0.92rem;
        }
    }
    .stButton>button {
        border-radius: 6px;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# Session State Initialization
if 'active_nav' not in st.session_state:
    st.session_state.active_nav = "Diagnostic Scanner"
if 'selected_disease_tab' not in st.session_state:
    st.session_state.selected_disease_tab = "CMD"

# Sidebar Setup
with st.sidebar:
    st.title("WCC")
    st.caption("West Nile Cassava Monitoring")
        
    st.markdown("---")
    
    nav_options = [
        "Diagnostic Scanner",
        "Disease Reference Guide",
        "Best Model Metrics & Benchmark",
        "About & Contributions"
    ]
    
    selected_nav = st.radio(
        "Navigation Menu",
        nav_options,
        index=nav_options.index(st.session_state.active_nav) if st.session_state.active_nav in nav_options else 0,
        key="nav_radio"
    )
    st.session_state.active_nav = selected_nav
    
    st.markdown("---")
    
    st.markdown("---")
    st.caption("Location: West Nile Region, Uganda")
    st.caption("Supported by War Child Canada School Feeding Project")

# Load Cached Model
model_res = load_cassava_model()
if len(model_res) == 4:
    model, model_name, target_size, is_real_model = model_res
else:
    model, model_name, target_size = model_res
    is_real_model = (model is not None)


# TAB 1: DIAGNOSTIC SCANNER
if st.session_state.active_nav == "Diagnostic Scanner":
    st.markdown("<h1 class='main-header'>Cassava Leaf Disease Diagnostic Scanner</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-header'>Upload or capture a photo of a cassava leaf to detect diseases and receive instant management recommendations.</p>", unsafe_allow_html=True)
    
    if not is_real_model:
        st.warning("""
        Model File Missing (EffNetB0_512_16.h5 not found in models/)!
        
        The app is running in Demo Fallback Mode. To load the exact predictions from your Colab notebook, run this command in your terminal:
        python download_models.py
        
        Then restart Streamlit.
        """)
        
    col_input, col_result = st.columns([1, 1.2])
    
    with col_input:
        st.markdown("### Upload or Capture Image")
        input_type = st.radio("Choose Input Method", ["Upload Photo", "Use Camera"], horizontal=True)
        
        uploaded_image = None
        if input_type == "Upload Photo":
            uploaded_file = st.file_uploader("Upload a cassava leaf photo (.jpg, .jpeg, .png)", type=["jpg", "jpeg", "png"])
            if uploaded_file is not None:
                uploaded_image = Image.open(uploaded_file)
        else:
            camera_file = st.camera_input("Capture leaf photo")
            if camera_file is not None:
                uploaded_image = Image.open(camera_file)
                
        if uploaded_image is not None:
            render_image(uploaded_image, caption="Uploaded Leaf Image")
        else:
            st.info("Tip: For best results, capture a single leaf flat in bright daylight without soil, hands, or background clutter.")
            
    with col_result:
        st.markdown("### Diagnostic Analysis & Results")
        
        if uploaded_image is not None:
            with st.spinner(f"Analyzing leaf patterns using {model_name}..."):
                res = predict_disease(uploaded_image, model=model, target_size=target_size)
                
            pred_key = res['predicted_key']
            details = res['details']
            confidence = res['confidence']
            prob_dict = res['prob_dict']
            
            if pred_key == 'Healthy':
                st.success(f"Diagnosis: Healthy Cassava Leaf ({confidence:.1%} Confidence)")
            elif pred_key == 'Retake':
                st.warning(f"Diagnosis: Unclear / Low Confidence Scan ({confidence:.1%} Top Signal)")
            else:
                st.error(f"Diagnosis: {details['name']} ({confidence:.1%} Confidence)")
                
            st.caption(f"Active Model Engine: {model_name} (Input Resolution: {target_size[0]}x{target_size[1]}px)")
            
            c1, c2 = st.columns(2)
            with c1:
                render_result_metric("Disease Type", details.get('type', 'N/A'))
            with c2:
                render_result_metric("Severity Level", details.get('severity', 'N/A'))
            
            st.markdown("#### Recommended Actions & Treatments")
            for idx, rec in enumerate(details.get('quick_advice', details.get('treatments', [])), 1):
                st.markdown(f"**{idx}.** {rec}")
                
            if pred_key in ['CMD', 'CBSD', 'CBB', 'CGM', 'Healthy']:
                st.markdown("---")
                if st.button(f"Read Full NARO Reference Notes on {FULL_NAMES[pred_key]}", type="primary"):
                    st.session_state.selected_disease_tab = pred_key
                    st.session_state.active_nav = "Disease Reference Guide"
                    st.rerun()
                    
            with st.expander("View Detailed Model Probability Breakdown", expanded=True):
                df_probs = pd.DataFrame({
                    'Condition': [FULL_NAMES.get(k, k) for k in prob_dict.keys()],
                    'Code': list(prob_dict.keys()),
                    'Probability': [f"{v:.1%}" for v in prob_dict.values()],
                    'Raw Value': [v * 100 for v in prob_dict.values()]
                }).sort_values(by='Raw Value', ascending=True)
                
                if HAS_PLOTLY:
                    fig = px.bar(
                        df_probs,
                        x='Raw Value',
                        y='Code',
                        orientation='h',
                        text=df_probs['Raw Value'].apply(lambda x: f"{x:.1f}%"),
                        color='Raw Value',
                        color_continuous_scale='Greens',
                        labels={'Raw Value': 'Probability (%)', 'Code': 'Condition'},
                        title="Interactive Diagnostic Confidence Distribution"
                    )
                    fig.update_layout(showlegend=False, height=280, margin=dict(l=20, r=20, t=40, b=20))
                    render_plotly(fig)
                else:
                    render_dataframe(df_probs[['Condition', 'Code', 'Probability']])
                    st.bar_chart(df_probs.set_index('Code')['Raw Value'])
                
        else:
            st.info("Please upload or capture an image on the left panel to begin diagnosis.")


# TAB 2: DISEASE REFERENCE GUIDE
elif st.session_state.active_nav == "Disease Reference Guide":
    st.markdown("<h1 class='main-header'>Cassava Pests & Diseases Reference Guide</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-header'>Comprehensive field guidelines, symptoms, vectors, and management practices derived from NARO (National Agricultural Research Organisation) research.</p>", unsafe_allow_html=True)
    
    disease_order = ["CMD", "CBSD", "CBB", "CGM", "Healthy"]
    
    tab_list = st.tabs([
        "1. Mosaic (CMD)",
        "2. Brown Streak (CBSD)",
        "3. Bacterial Blight (CBB)",
        "4. Green Mite (CGM)",
        "5. Healthy Leaf & Practices"
    ])
    
    for idx, d_code in enumerate(disease_order):
        d_info = DISEASE_DETAILS[d_code]
        with tab_list[idx]:
            st.markdown(f"## {d_info['name']}")
            st.caption(f"Causative Agent: **{d_info['causative_agent']}** | Category: **{d_info['type']}**")
            
            c_left, c_right = st.columns([1.2, 1])
            
            with c_left:
                st.markdown("### Key Visual Symptoms")
                for item in d_info['symptoms']:
                    st.markdown(f"- {item}")
                    
                st.markdown("### Spread & Vector Mechanism")
                for item in d_info['spread_vectors']:
                    st.markdown(f"- {item}")
                    
                st.markdown("### Economic & Yield Impact")
                st.warning(d_info['yield_impact'])
                
            with c_right:
                st.markdown("### Recommended Control & Management")
                for idx_t, treatment in enumerate(d_info['treatments'], 1):
                    st.markdown(f"**{idx_t}.** {treatment}")
                    
                if d_code != 'Healthy':
                    st.info("IPM Principle: Combine clean planting material with early roguing and whitefly monitoring for optimal control.")


# TAB 3: BEST MODEL METRICS & BENCHMARK
elif st.session_state.active_nav == "Best Model Metrics & Benchmark":
    st.markdown("<h1 class='main-header'>Best Model Performance Metrics (EffNetB0_512_16)</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-header'>Detailed evaluation metrics for the recommended Best Model (EfficientNet-B0 512px input) evaluated on 4,279 unseen test photos.</p>", unsafe_allow_html=True)
    
    # Top KPI Metrics Cards
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Overall Accuracy", "87.52%")
    m2.metric("Macro F1-Score", "77.34%")
    m3.metric("Macro ROC-AUC", "96.99%")
    m4.metric("Diseased Called Healthy", "5.44%", delta="-0.26% vs ensemble", delta_color="inverse")
    
    st.markdown("---")
    st.markdown("### Class-by-Class Classification Performance")
    
    # Notebook Classification Report Data for Best Model
    best_class_metrics = {
        'Condition': ['Cassava Bacterial Blight (CBB)', 'Cassava Brown Streak Disease (CBSD)', 'Cassava Green Mite / Mottle (CGM)', 'Cassava Mosaic Disease (CMD)', 'Healthy Leaf'],
        'Class Code': ['CBB', 'CBSD', 'CGM', 'CMD', 'Healthy'],
        'Precision (%)': [60.0, 79.2, 87.7, 96.0, 65.8],
        'Recall / Sensitivity (%)': [63.0, 78.7, 72.3, 95.6, 77.5],
        'F1-Score (%)': [61.5, 78.9, 79.3, 95.8, 71.2],
        'Test Photos Support': [200, 436, 495, 2638, 510]
    }
    
    df_best = pd.DataFrame(best_class_metrics)
    render_dataframe(df_best)
    
    if HAS_PLOTLY:
        st.markdown("#### Interactive Class-by-Class Recall & Precision")
        fig_best = px.bar(
            df_best,
            x='Class Code',
            y=['Precision (%)', 'Recall / Sensitivity (%)', 'F1-Score (%)'],
            barmode='group',
            title="Best Model (EffNetB0_512_16) Precision, Recall & F1-Score by Condition",
            labels={'value': 'Score (%)', 'Class Code': 'Condition Code'}
        )
        render_plotly(fig_best)
        
    st.markdown("---")
    st.markdown("### Safety-First Evaluation View")
    
    safety_summary = {
        'Group Meaning': ['Diseased, called Diseased (True Positive)', 'Diseased, called HEALTHY (Dangerous Error / False Negative)', 'Healthy, called Diseased (False Alarm / False Positive)', 'Healthy, called Healthy (True Negative)'],
        'Photo Count': [3564, 205, 115, 395],
        '% of All 4,279 Test Photos': ['83.29%', '4.79%', '2.69%', '9.23%'],
        '% of Group': ['94.56%', '5.44%', '22.55%', '77.45%']
    }
    render_dataframe(pd.DataFrame(safety_summary))
    
    st.info("""
    Safety Rule Choice: In cassava disease monitoring, false reassurance (calling a diseased plant 'Healthy') is the most dangerous error because farmers risk propagating infected stem cuttings.
    
    The Original EfficientNet-B0 model (EffNetB0_512_16.h5) achieved the lowest share of diseased plants called healthy (5.44% = 205 of 3769 diseased photos) with 95% Confidence Interval (4.8% to 6.2%).
    """)


# TAB 4: ABOUT, PROJECT & CONTRIBUTIONS
elif st.session_state.active_nav == "About & Contributions":
    st.markdown("<h1 class='main-header'>About & Project Contributions</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-header'>AI-Assisted Cassava Leaf Disease Monitoring in West Nile, Uganda.</p>", unsafe_allow_html=True)
    
    col_about1, col_about2 = st.columns([1.2, 1])
    
    with col_about1:
        st.markdown("### War Child Canada - West Nile Project")
        st.markdown("""
        This application supports the **War Child Canada School Feeding & Agricultural Resilience Project** in West Nile, Uganda.
        
        Cassava is a vital food security crop in East Africa. However, viral diseases (CMD, CBSD) and pests cause devastating yield losses. By providing rural farmers, agricultural extension workers, and school garden managers with accessible AI-powered diagnostic tools, we aim to detect disease outbreaks early and protect food supplies.
        """)
        
        st.markdown("### Project Repository & Author")
        st.markdown("""
        - **GitHub Repository**: [Josh-robins/Cassava-Leaf-Disease-Classification](https://github.com/Josh-robins/Cassava-Leaf-Disease-Classification)
        - **Author / Lead**: Reach out to [@josh-robins](https://github.com/Josh-robins) on GitHub for contributions or inquiries.
        """)
        
    with col_about2:
        st.markdown("### Disclaimer & Call for Contributions")
        st.info("""
        Disclaimer: This is a project under active development. Predictions serve as screening aids and should be confirmed with agricultural extension officers or NARO experts.
        """)
        
        st.markdown("""
        #### Open for Contributions!
        We warmly welcome contributions from:
        - **Agronomists & Plant Pathologists** (disease validation & field advice)
        - **Data Analysts & ML Engineers** (model optimization & dataset expansion)
        - **System Architects & Software Engineers** (app features & mobile deployment)
        - **Project Managers & Field Officers** (community rollout & user testing)
        
        Connect via [@josh-robins GitHub](https://github.com/Josh-robins) to join the initiative.
        """)

# Footer
st.markdown("---")
st.caption("Cassava Disease Diagnostic System | War Child Canada & NARO | West Nile, Uganda")
