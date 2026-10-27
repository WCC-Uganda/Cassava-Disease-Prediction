# Cassava Disease Prediction System

An AI-powered web application for real-time cassava leaf disease detection, agricultural field advice, and disease reference guidance. Developed for the War Child Canada School Feeding & West Nile Cassava Monitoring Project in Uganda.

---

## Features

1. Fast Diagnostic Scanner:
   - Upload or capture a cassava leaf photo directly using camera or file upload.
   - Powered by the Best Model (EffNetB0_512_16.h5) with 512x512 resolution input, achieving 87.52% Accuracy and the lowest rate of false reassurance (5.44% diseased called healthy).
   - Fast sub-second page refreshes powered by Streamlit @st.cache_resource memory caching.
   - Evaluates disease probability across 5 classes:
     - CMD: Cassava Mosaic Disease
     - CBSD: Cassava Brown Streak Disease
     - CBB: Cassava Bacterial Blight
     - CGM: Cassava Green Mite / Mottle
     - Healthy: Healthy Leaf
   - Applies safety confidence thresholds (0.60 disease threshold, 0.80 healthy threshold) to prevent false reassurance.

2. NARO Disease Reference Guide:
   - Detailed disease notes, symptoms, causative pathogens, spread vectors, and management options extracted from NARO (Dr. Alex Abaca) research guidelines.
   - Instant deep-links from diagnostic prediction results to specific disease reference tabs.

3. Best Model Performance & Benchmarks:
   - Detailed class-by-class evaluation metrics (Precision, Recall, F1-Score, Support) for the Best Model (EffNetB0_512_16.h5).
   - Interactive Plotly visualizations and safety-first confusion matrix metrics.

4. Project Context & Contributions:
   - Context on War Child Canada's agricultural resilience and school feeding initiative.
   - Direct link to GitHub repository and contribution guidelines for Agronomists, Data Analysts, System Architects, and Project Managers.

---

## Step-by-Step Setup Guide

### 1. Open Terminal in Project Folder
Navigate into the project folder:
```bash
cd Cassava_Disease_Prediction
```

### 2. Create and Activate a Virtual Environment
Creating a Python virtual environment keeps your project dependencies isolated.

On Linux / macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

On Windows (Command Prompt / PowerShell):
```cmd
python -m venv venv
venv\Scripts\activate
```

### 3. Install Required Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Download the Best Model (EffNetB0_512_16.h5)
Run the automated downloader script to fetch the best trained model (EffNetB0_512_16.h5) directly into the models/ directory:
```bash
python download_models.py
```

### 5. Launch the Streamlit App Locally
```bash
streamlit run app.py
```
Your web browser will automatically open http://localhost:8501.

---

## Publishing to GitHub & Streamlit Cloud

### 1. Push to GitHub Repository
In your terminal, commit and push your project to your GitHub repository:
```bash
git add .
git commit -m "Add Cassava Disease Prediction Streamlit app"
git push origin main
```

### 2. Deploy on Streamlit Cloud
1. Go to share.streamlit.io and sign in with GitHub.
2. Click New app.
3. Fill in the details:
   - Repository: Josh-robins/Cassava-Leaf-Disease-Classification
   - Branch: main
   - Main file path: app.py
4. Click Deploy!

---

## Project Disclaimer & Contributions

> Disclaimer: This application is a screening aid under active development. Contributions are welcome from Agronomists, Data Analysts, System Architects, and Project Managers.

Reach out to @josh-robins on GitHub to contribute or collaborate!
