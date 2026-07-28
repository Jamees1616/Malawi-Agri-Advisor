"""
Malawi district location database.

Used to connect a farmer's selected district
to representative coordinates for weather data.
"""

MALAWI_DISTRICTS = {
    "dedza": {
        "name": "Dedza",
        "region": "Central Region",
        "latitude": -14.3779,
        "longitude": 34.3332
    },
    "dowa": {
        "name": "Dowa",
        "region": "Central Region",
        "latitude": -13.6539,
        "longitude": 33.9370
    },
    "kasungu": {
        "name": "Kasungu",
        "region": "Central Region",
        "latitude": -13.0333,
        "longitude": 33.4833
    },
    "lilongwe": {
        "name": "Lilongwe",
        "region": "Central Region",
        "latitude": -13.9626,
        "longitude": 33.7741
    },
    "mchinji": {
        "name": "Mchinji",
        "region": "Central Region",
        "latitude": -13.7984,
        "longitude": 32.8800
    },
    "nkhotakota": {
        "name": "Nkhotakota",
        "region": "Central Region",
        "latitude": -12.9274,
        "longitude": 34.2961
    },
    "ntchisi": {
        "name": "Ntchisi",
        "region": "Central Region",
        "latitude": -13.3436,
        "longitude": 34.2555
    },
    "ntcheu": {
        "name": "Ntcheu",
        "region": "Central Region",
        "latitude": -14.8203,
        "longitude": 34.6359
    },
    "salima": {
        "name": "Salima",
        "region": "Central Region",
        "latitude": -13.7803,
        "longitude": 34.4580
    },

    "chitipa": {
        "name": "Chitipa",
        "region": "Northern Region",
        "latitude": -9.7020,
        "longitude": 33.2697
    },
    "karonga": {
        "name": "Karonga",
        "region": "Northern Region",
        "latitude": -9.9333,
        "longitude": 33.9333
    },
    "likoma": {
        "name": "Likoma",
        "region": "Northern Region",
        "latitude": -12.0583,
        "longitude": 34.7358
    },
    "mzimba": {
        "name": "Mzimba",
        "region": "Northern Region",
        "latitude": -11.9000,
        "longitude": 33.6000
    },
    "nkhata_bay": {
        "name": "Nkhata Bay",
        "region": "Northern Region",
        "latitude": -11.6066,
        "longitude": 34.2900
    },
    "rumphi": {
        "name": "Rumphi",
        "region": "Northern Region",
        "latitude": -11.0170,
        "longitude": 33.8570
    },

    "balaka": {
        "name": "Balaka",
        "region": "Southern Region",
        "latitude": -14.9833,
        "longitude": 34.9500
    },
    "blantyre": {
        "name": "Blantyre",
        "region": "Southern Region",
        "latitude": -15.7861,
        "longitude": 35.0058
    },
    "chikwawa": {
        "name": "Chikwawa",
        "region": "Southern Region",
        "latitude": -16.0333,
        "longitude": 34.8000
    },
    "chiradzulu": {
        "name": "Chiradzulu",
        "region": "Southern Region",
        "latitude": -15.7000,
        "longitude": 35.1833
    },
    "machinga": {
        "name": "Machinga",
        "region": "Southern Region",
        "latitude": -15.1685,
        "longitude": 35.3000
    },
    "mangochi": {
        "name": "Mangochi",
        "region": "Southern Region",
        "latitude": -14.4782,
        "longitude": 35.2645
    },
    "mulanje": {
        "name": "Mulanje",
        "region": "Southern Region",
        "latitude": -16.0316,
        "longitude": 35.5000
    },
    "mwanza": {
        "name": "Mwanza",
        "region": "Southern Region",
        "latitude": -15.6167,
        "longitude": 34.5167
    },
    "nsanje": {
        "name": "Nsanje",
        "region": "Southern Region",
        "latitude": -16.9167,
        "longitude": 35.2667
    },
    "phalombe": {
        "name": "Phalombe",
        "region": "Southern Region",
        "latitude": -15.8000,
        "longitude": 35.6500
    },
    "thyolo": {
        "name": "Thyolo",
        "region": "Southern Region",
        "latitude": -16.0667,
        "longitude": 35.1333
    },
    "zomba": {
        "name": "Zomba",
        "region": "Southern Region",
        "latitude": -15.3850,
        "longitude": 35.3188
    }
}


def normalize_district_name(district):
    """
    Normalize a district name for searching.
    """

    if not district:
        return None

    return (
        district
        .strip()
        .lower()
        .replace("-", "_")
        .replace(" ", "_")
    )


def get_district(district):
    """
    Return location information for a district.
    """

    key = normalize_district_name(
        district
    )

    if not key:
        return None

    return MALAWI_DISTRICTS.get(
        key
    )


def get_all_locations():
    """
    Return all district locations.
    """

    return list(
        MALAWI_DISTRICTS.values()
    )
