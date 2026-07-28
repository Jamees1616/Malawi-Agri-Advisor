"""
Malawi Agriculture Knowledge Base
---------------------------------

Structured agricultural information for the Malawi Agri Advisor platform.

This module provides:
- Malawi regions and districts
- Major crops
- Crop growing information
- General planting guidance
- Soil considerations
- Rainfall requirements
- Crop maturity periods

Important:
This is a foundational knowledge layer.
AI-generated advice should use this data as context and should
not replace recommendations from agricultural extension officers.
"""


# ============================================================
# MALAWI REGIONS AND DISTRICTS
# ============================================================

MALAWI_REGIONS = {
    "Northern Region": [
        "Chitipa",
        "Karonga",
        "Likoma",
        "Mzimba",
        "Nkhata Bay",
        "Rumphi"
    ],

    "Central Region": [
        "Dedza",
        "Dowa",
        "Kasungu",
        "Lilongwe",
        "Mchinji",
        "Nkhotakota",
        "Ntcheu",
        "Ntchisi",
        "Salima"
    ],

    "Southern Region": [
        "Balaka",
        "Blantyre",
        "Chikwawa",
        "Chiradzulu",
        "Machinga",
        "Mangochi",
        "Mulanje",
        "Mwanza",
        "Neno",
        "Nsanje",
        "Phalombe",
        "Thyolo",
        "Zomba"
    ]
}


# ============================================================
# MAJOR CROPS
# ============================================================

CROPS = {

    "maize": {
        "name": "Maize",
        "local_names": {
            "english": "Maize",
            "chichewa": "Chimanga"
        },

        "category": "Cereal",

        "importance": (
            "Maize is one of the most important staple food crops "
            "in Malawi."
        ),

        "planting_window": (
            "Generally planted at the beginning of the main rainy season. "
            "Farmers should use locally recommended planting dates and "
            "consider the onset of reliable rains."
        ),

        "rainfall_requirement": (
            "Requires adequate moisture during establishment, vegetative "
            "growth and especially around flowering and grain filling."
        ),

        "soil": (
            "Performs best in fertile, well-drained soils with good "
            "moisture-holding capacity."
        ),

        "temperature": (
            "Warm growing conditions are generally suitable, but extreme "
            "heat during flowering can reduce yield."
        ),

        "maturity": (
            "Maturity varies significantly by variety, from early-maturing "
            "to medium- and late-maturing varieties."
        ),

        "key_advice": [
            "Use certified or quality seed from reliable sources.",
            "Choose varieties suited to the local agro-ecological conditions.",
            "Plant when adequate soil moisture is available.",
            "Use recommended spacing for the selected variety.",
            "Apply nutrients based on soil fertility and local recommendations.",
            "Control weeds early to reduce competition.",
            "Monitor for fall armyworm and other pests.",
            "Harvest at the appropriate maturity stage and dry grain properly."
        ]
    },


    "groundnuts": {
        "name": "Groundnuts",
        "local_names": {
            "english": "Groundnuts",
            "chichewa": "Mtedza"
        },

        "category": "Legume",

        "importance": (
            "Groundnuts are an important food and cash crop and can "
            "contribute to household nutrition and income."
        ),

        "planting_window": (
            "Generally planted during the rainy season when soil moisture "
            "is sufficient for germination and early growth."
        ),

        "rainfall_requirement": (
            "Requires adequate moisture during establishment and flowering, "
            "while excessive waterlogging should be avoided."
        ),

        "soil": (
            "Light to medium-textured, well-drained soils are generally "
            "preferred, particularly soils that allow easy pod development "
            "and harvesting."
        ),

        "temperature": (
            "Warm conditions are generally suitable."
        ),

        "maturity": (
            "Variety-dependent; farmers should follow the recommended "
            "maturity period for their selected variety."
        ),

        "key_advice": [
            "Use quality seed suited to the production area.",
            "Avoid poorly drained fields.",
            "Practice timely weeding.",
            "Use recommended spacing.",
            "Monitor for fungal diseases and insect pests.",
            "Rotate crops where appropriate.",
            "Dry harvested groundnuts properly to reduce mould and aflatoxin risk."
        ]
    },


    "soybean": {
        "name": "Soybean",
        "local_names": {
            "english": "Soybean",
            "chichewa": "Soya"
        },

        "category": "Legume",

        "importance": (
            "Soybean is an important legume crop with uses in food, "
            "animal feed and commercial processing."
        ),

        "planting_window": (
            "Generally planted during the rainy season when sufficient "
            "soil moisture is available."
        ),

        "rainfall_requirement": (
            "Requires adequate moisture throughout establishment and "
            "reproductive growth, while avoiding prolonged waterlogging."
        ),

        "soil": (
            "Generally performs well in fertile, well-drained soils."
        ),

        "temperature": (
            "Moderate to warm growing conditions are generally suitable."
        ),

        "maturity": (
            "Variety-dependent."
        ),

        "key_advice": [
            "Use quality seed of an adapted variety.",
            "Use appropriate inoculation practices where recommended.",
            "Maintain good weed control.",
            "Avoid prolonged waterlogging.",
            "Rotate with other crops where practical.",
            "Harvest at the correct maturity stage."
        ]
    },


    "beans": {
        "name": "Common Beans",
        "local_names": {
            "english": "Beans",
            "chichewa": "Nyemba"
        },

        "category": "Legume",

        "importance": (
            "Beans are an important source of dietary protein and "
            "can contribute to household food security and income."
        ),

        "planting_window": (
            "Planting depends on the production system and local rainfall "
            "conditions. Farmers should use locally recommended planting "
            "windows."
        ),

        "rainfall_requirement": (
            "Requires sufficient moisture but is sensitive to excessive "
            "waterlogging."
        ),

        "soil": (
            "Generally performs well in fertile, well-drained soils."
        ),

        "temperature": (
            "Moderate temperatures are generally preferred."
        ),

        "maturity": (
            "Variety-dependent."
        ),

        "key_advice": [
            "Use quality seed.",
            "Plant in well-drained fields.",
            "Control weeds early.",
            "Monitor for bean pests and diseases.",
            "Avoid planting continuously on the same land where disease "
            "pressure is a concern.",
            "Harvest and dry properly to maintain grain quality."
        ]
    },


    "cassava": {
        "name": "Cassava",
        "local_names": {
            "english": "Cassava",
            "chichewa": "Chinangwa"
        },

        "category": "Root Crop",

        "importance": (
            "Cassava is an important food-security crop and can provide "
            "food during periods when other crops are affected by drought."
        ),

        "planting_window": (
            "Planting should be timed according to local rainfall and "
            "availability of sufficient soil moisture for establishment."
        ),

        "rainfall_requirement": (
            "Cassava can tolerate relatively dry conditions once established, "
            "but adequate moisture is important during establishment."
        ),

        "soil": (
            "Can grow in a range of soils but performs better in "
            "well-drained soils."
        ),

        "temperature": (
            "Warm tropical conditions are generally suitable."
        ),

        "maturity": (
            "Harvest timing depends on variety and intended use."
        ),

        "key_advice": [
            "Use healthy planting material.",
            "Select varieties adapted to local conditions.",
            "Plant in well-prepared soil.",
            "Control weeds during early establishment.",
            "Monitor for cassava pests and diseases.",
            "Use disease-free planting material where possible."
        ]
    },


    "sweet_potato": {
        "name": "Sweet Potato",
        "local_names": {
            "english": "Sweet Potato",
            "chichewa": "Mbatata"
        },

        "category": "Root Crop",

        "importance": (
            "Sweet potato contributes to food security and can provide "
            "important nutritional benefits."
        ),

        "planting_window": (
            "Planting should be scheduled when sufficient moisture is "
            "available for vine establishment."
        ),

        "rainfall_requirement": (
            "Requires adequate moisture during establishment and tuber "
            "development, while avoiding prolonged waterlogging."
        ),

        "soil": (
            "Loose, well-drained soils are generally suitable for good "
            "root development."
        ),

        "temperature": (
            "Warm conditions are generally suitable."
        ),

        "maturity": (
            "Variety-dependent."
        ),

        "key_advice": [
            "Use healthy vines or quality planting material.",
            "Plant in well-prepared soil.",
            "Control weeds early.",
            "Monitor for sweet potato pests and diseases.",
            "Use crop rotation where appropriate.",
            "Harvest according to the variety and intended market."
        ]
    },


    "rice": {
        "name": "Rice",
        "local_names": {
            "english": "Rice",
            "chichewa": "Mpunga"
        },

        "category": "Cereal",

        "importance": (
            "Rice is an important food crop and is produced under "
            "different production systems in suitable areas."
        ),

        "planting_window": (
            "Timing depends strongly on the production system, water "
            "availability and local growing conditions."
        ),

        "rainfall_requirement": (
            "Requires reliable water availability during the production "
            "cycle, depending on whether production is rainfed or irrigated."
        ),

        "soil": (
            "Suitable soils depend on the production system. Water management "
            "and drainage are important considerations."
        ),

        "temperature": (
            "Warm growing conditions are generally suitable."
        ),

        "maturity": (
            "Variety-dependent."
        ),

        "key_advice": [
            "Use quality seed.",
            "Select varieties suited to the local production environment.",
            "Manage water carefully.",
            "Control weeds effectively.",
            "Monitor for pests and diseases.",
            "Harvest and dry grain properly to maintain quality."
        ]
    },


    "tobacco": {
        "name": "Tobacco",
        "local_names": {
            "english": "Tobacco",
            "chichewa": "Fodya"
        },

        "category": "Commercial Crop",

        "importance": (
            "Tobacco has historically been an important commercial crop "
            "in Malawi."
        ),

        "planting_window": (
            "Production timing depends on the tobacco type, nursery "
            "management and local agronomic recommendations."
        ),

        "rainfall_requirement": (
            "Requires appropriate moisture management throughout production."
        ),

        "soil": (
            "Soil requirements vary by tobacco type and production system."
        ),

        "temperature": (
            "Warm growing conditions are generally suitable."
        ),

        "maturity": (
            "Depends on tobacco type and production system."
        ),

        "key_advice": [
            "Use recommended agronomic practices.",
            "Follow local extension guidance.",
            "Manage soil fertility responsibly.",
            "Monitor pests and diseases.",
            "Follow applicable regulations and sustainable production practices."
        ]
    }
}


# ============================================================
# GENERAL FARMING GUIDANCE
# ============================================================

GENERAL_FARMING_GUIDANCE = {

    "soil_health": [
        "Maintain soil organic matter where possible.",
        "Use crop rotation to support soil health.",
        "Reduce unnecessary soil disturbance.",
        "Use compost or organic amendments where appropriate.",
        "Consider soil testing when available.",
        "Use fertilizer according to crop needs and local recommendations."
    ],

    "water_management": [
        "Monitor rainfall and soil moisture.",
        "Use water conservation practices where appropriate.",
        "Avoid unnecessary water loss.",
        "Protect fields from erosion.",
        "Use irrigation efficiently where irrigation is available."
    ],

    "climate_smart_agriculture": [
        "Choose crop varieties suited to local climate conditions.",
        "Use drought-tolerant varieties where appropriate.",
        "Diversify crops to reduce production risk.",
        "Practice soil and water conservation.",
        "Use weather information to support farm decisions."
    ],

    "pest_management": [
        "Inspect crops regularly.",
        "Identify pests before applying control measures.",
        "Use integrated pest management principles.",
        "Follow label instructions when using approved pesticides.",
        "Use protective equipment when handling agricultural chemicals.",
        "Seek advice from agricultural extension officers when pest problems "
        "are difficult to identify or control."
    ],

    "disease_management": [
        "Use healthy seed and planting materials.",
        "Maintain field hygiene.",
        "Rotate crops where appropriate.",
        "Monitor crops regularly.",
        "Remove and manage severely affected plants according to recommended "
        "agricultural practices.",
        "Seek professional agricultural advice when disease diagnosis is uncertain."
    ]
}


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def get_all_districts():
    """
    Return a flat list of all districts in Malawi.
    """

    districts = []

    for region_districts in MALAWI_REGIONS.values():
        districts.extend(region_districts)

    return districts


def get_region_by_district(district):
    """
    Find the region that contains a given district.
    """

    district = district.strip().lower()

    for region, districts in MALAWI_REGIONS.items():
        for item in districts:
            if item.lower() == district:
                return region

    return None


def get_crop(crop_name):
    """
    Retrieve crop information by crop name.
    """

    crop_name = crop_name.strip().lower()

    return CROPS.get(crop_name)


def get_crop_names():
    """
    Return a list of available crop identifiers.
    """

    return list(CROPS.keys())
