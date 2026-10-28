CLASS_SHORT = ['CBB', 'CBSD', 'CGM', 'CMD', 'Healthy']

FULL_NAMES = {
    'CMD': 'Cassava Mosaic Disease',
    'CBSD': 'Cassava Brown Streak Disease',
    'CBB': 'Cassava Bacterial Blight',
    'CGM': 'Cassava Green Mite / Mottle',
    'Healthy': 'Healthy Cassava Leaf'
}

DISEASE_DETAILS = {
    'CMD': {
        'name': 'Cassava Mosaic Disease (CMD)',
        'short_code': 'CMD',
        'causative_agent': 'Cassava mosaic Begomoviruses (CMBs)',
        'type': 'Viral Disease',
        'severity': 'Critical',
        'yield_impact': 'Up to 90-100% loss in susceptible varieties',
        'symptoms': [
            'Distinctive yellow-green chlorotic mosaic patterns on leaves.',
            'Severe leaf distortion, twisting, and reduction in leaf size.',
            'Stunting of infected young plants.',
            'Total leaf loss leaving bare stems (candle stick effect).'
        ],
        'spread_vectors': [
            'Whiteflies (Bemisia tabaci) feeding on young upper leaves.',
            'Use of infected stem cuttings for propagation.'
        ],
        'treatments': [
            'Uproot (rogue) affected plants early and burn or bury them immediately.',
            'Never use stems from infected plants as planting material or cuttings.',
            'Replant exclusively with clean, CMD-resistant cassava varieties from certified multipliers (NARO / NaCRRI).',
            'Inspect gardens bi-weekly for whitefly infestations and rogue newly infected plants promptly.'
        ],
        'quick_advice': [
            "Uproot affected plants early and burn or bury them; never use their stems as cuttings.",
            "Replant with clean, CMD-resistant varieties from a trusted multiplier.",
            "Whiteflies spread CMD: inspect the garden every two weeks and remove new sick plants quickly."
        ]
    },
    'CBSD': {
        'name': 'Cassava Brown Streak Disease (CBSD)',
        'short_code': 'CBSD',
        'causative_agent': 'Cassava brown streak viruses (CBSVs)',
        'type': 'Viral Disease',
        'severity': 'Extremely Critical',
        'yield_impact': 'Up to 100% loss; roots rot internally and become unpalatable/unsellable',
        'symptoms': [
            'Feathery chlorotic patches along secondary and tertiary leaf veins.',
            'Dark brown streaks or lesions on young green stems.',
            'Tuberous root constriction and internal dry brown corky flesh necrosis.',
            'Roots may rot entirely even when top leaves show only subtle symptoms.'
        ],
        'spread_vectors': [
            'Cassava whitefly vector (Bemisia tabaci).',
            'Transport and planting of infected stem cuttings.'
        ],
        'treatments': [
            'Uproot and burn infected plants early; inspect tuberous roots of nearby plants.',
            'Source clean cuttings only from certified CBSD-tolerant multipliers (NARO/NaCRRI).',
            'Do not share, sell, or transport stem cuttings from infected fields to prevent regional spread.',
            'Practice field isolation and sanitize tools after harvesting suspect fields.'
        ],
        'quick_advice': [
            "Uproot and destroy affected plants early; roots can rot even when leaves look fine, so check the roots of neighbouring plants.",
            "Replant only clean cuttings of CBSD-tolerant varieties from a trusted multiplier (ask NaCRRI / your extension officer).",
            "Whiteflies spread it: do not share or sell cuttings from this garden, and ask an extension officer to inspect nearby gardens."
        ]
    },
    'CBB': {
        'name': 'Cassava Bacterial Blight (CBB)',
        'short_code': 'CBB',
        'causative_agent': 'Bacterium (Xanthomonas axonopodis pv. manihotis)',
        'type': 'Bacterial Disease',
        'severity': 'High',
        'yield_impact': '20% to 100% loss under wet, humid conditions',
        'symptoms': [
            'Angular water-soaked leaf spots that brown and dry out.',
            'Wilting, yellowing, and blighting of entire leaves.',
            'Yellowish gum exudation (droplets) on stems and leaf petioles.',
            'Dieback of shoots and vascular necrosis in green stems.'
        ],
        'spread_vectors': [
            'Rain splashes carrying bacterial droplets across healthy plants.',
            'Contaminated farming tools (knives, cutlasses, hoes).',
            'Infected planting cuttings, stem scratches, and mechanical damage.'
        ],
        'treatments': [
            'Cut out and burn or bury affected plants and prunings immediately.',
            'Disinfect farm tools (knives, hoes) with household bleach or soapy water between plants.',
            'Avoid working in cassava gardens when foliage is wet to prevent bacterial spread.',
            'Rotate crops with non-host plants (e.g., maize or beans) during the next planting season.',
            'Plant clean, disease-free cuttings sourced from verified disease-free gardens.'
        ],
        'quick_advice': [
            "Cut out and burn or bury affected plants and prunings now; do not leave them in or near the garden.",
            "Plant only clean cuttings from healthy gardens, and wash knives and hoes with soap or bleach between plants.",
            "Avoid working in the garden when leaves are wet, and rotate with a non-host crop such as beans or maize next season."
        ]
    },
    'CGM': {
        'name': 'Cassava Green Mite / Mottle (CGM)',
        'short_code': 'CGM',
        'causative_agent': 'Mite pest (Mononychellus tanajoa)',
        'type': 'Arthropod Pest Damage',
        'severity': 'Moderate to High',
        'yield_impact': 'Up to 80-85% loss in severe dry season infestations',
        'symptoms': [
            'Pinprick yellow speckled chlorosis on upper surfaces of young terminal leaves.',
            'Leaves become small, narrow, deformed, and stunted (shoe-string appearance).',
            'Terminal shoot tips die off, causing complete defoliation (candle stick).',
            'Reduced leaf area severely inhibits photosynthesis.'
        ],
        'spread_vectors': [
            'Wind dispersal of tiny green mites across fields.',
            'Movement of infested planting materials during dry seasons.'
        ],
        'treatments': [
            'Inspect shoot tips and leaf undersides regularly for green mite populations.',
            'Do not take cuttings from badly infested or stunted plants.',
            'Biological control: introduce natural predator mites (Typhlodromalus aripo).',
            'Avoid chemical pesticide sprays that destroy natural beneficial predators.',
            'Time planting at the onset of rains and keep fields free of weeds.'
        ],
        'quick_advice': [
            "Check shoot tips and the underside of young leaves for tiny green mites, and ask your extension officer to confirm.",
            "Do not take cuttings from badly affected plants; plant at the start of the rains and choose tolerant varieties.",
            "Avoid spraying: it kills the natural enemies of the mite; keep the garden weeded and watch the dry-season spread."
        ]
    },
    'Healthy': {
        'name': 'Healthy Cassava Leaf',
        'short_code': 'Healthy',
        'causative_agent': 'None (Normal Leaf)',
        'type': 'Normal Plant',
        'severity': 'None',
        'yield_impact': 'Optimal potential yield expected',
        'symptoms': [
            'Vigorous, uniform dark green leaf blades.',
            'No chlorotic mosaic spots, vein yellowing, or leaf twisting.',
            'Clean stems free of brown streaks, lesions, or gum droplets.'
        ],
        'spread_vectors': [
            'N/A'
        ],
        'treatments': [
            'Maintain routine monitoring every two weeks, focusing on young shoots.',
            'Select planting cuttings exclusively from healthy, symptom-free plants.',
            'Ensure good soil fertility, proper field weeding, and crop isolation.'
        ],
        'quick_advice': [
            "No disease was found on this leaf; keep inspecting every two weeks, especially young shoots.",
            "Take cuttings only from plants with no yellow patches or streaks on leaves or stems.",
            "One leaf cannot show the stems or roots: if growth is poor or stems show brown streaks, ask your extension officer."
        ]
    },
    'Retake': {
        'name': 'Low Confidence / Unclear Photo',
        'short_code': 'Retake',
        'causative_agent': 'Uncertain Diagnostic Signal',
        'type': 'Scanning Quality Notice',
        'severity': 'Uncertain',
        'yield_impact': 'Re-inspection recommended',
        'symptoms': [
            'Image may be blurry, poorly lit, or occluded by hands, soil, or background noise.'
        ],
        'spread_vectors': [
            'N/A'
        ],
        'treatments': [
            'Retake the photo in bright daylight.',
            'Ensure a single cassava leaf is flat, centered, and well-focused.',
            'Avoid hands, soil, or background clutter covering the leaf.'
        ],
        'quick_advice': [
            "The model is not sure about this photo.",
            "Retake it in daylight: one whole leaf, flat and in focus, without hands or soil covering it.",
            "If the plant still looks unhealthy, show it to your extension officer."
        ]
    }
}
