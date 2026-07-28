from data.malawi_agriculture import (
    get_crop,
    get_region_by_district
)

from data.malawi_locations import (
    get_district
)


class ContextService:
    """
    Builds complete agricultural context for Malawi Agri Advisor.

    Combines:
    - Farmer location
    - Malawi region
    - District coordinates
    - Selected crop
    - Crop-specific agricultural knowledge
    """

    @staticmethod
    def build_context(
        district=None,
        crop=None,
        farmer_context=None
    ):

        context = {
            "location": {},
            "crop": {},
            "farmer": farmer_context or {}
        }

        # ----------------------------------------------
        # DISTRICT AND REGION
        # ----------------------------------------------

        if district:

            region = get_region_by_district(
                district
            )

            location = get_district(
                district
            )

            context["location"] = {
                "district": district,
                "region": region
            }

            if location:

                context["location"].update({
                    "official_name": location.get(
                        "name"
                    ),
                    "latitude": location.get(
                        "latitude"
                    ),
                    "longitude": location.get(
                        "longitude"
                    )
                })

        # ----------------------------------------------
        # CROP INFORMATION
        # ----------------------------------------------

        if crop:

            crop_data = get_crop(
                crop
            )

            if crop_data:

                context["crop"] = {
                    "requested_crop": crop,
                    "information": crop_data
                }

        return context


    @staticmethod
    def format_for_ai(
        context
    ):
        """
        Convert agricultural context into clean
        text suitable for the AI model.
        """

        sections = []

        # ----------------------------------------------
        # LOCATION
        # ----------------------------------------------

        location = context.get(
            "location",
            {}
        )

        if location:

            location_text = (
                f"District: "
                f"{location.get('official_name', 'Unknown')}\n"
                f"Region: "
                f"{location.get('region', 'Unknown')}\n"
                f"Latitude: "
                f"{location.get('latitude', 'Unknown')}\n"
                f"Longitude: "
                f"{location.get('longitude', 'Unknown')}"
            )

            sections.append(
                "FARMER LOCATION:\n"
                + location_text
            )

        # ----------------------------------------------
        # CROP
        # ----------------------------------------------

        crop = context.get(
            "crop",
            {}
        )

        if crop:

            crop_name = crop.get(
                "requested_crop"
            )

            crop_information = crop.get(
                "information",
                {}
            )

            crop_lines = []

            crop_lines.append(
                f"Crop: "
                f"{crop_information.get('name', crop_name)}"
            )

            local_names = (
                crop_information.get(
                    "local_names",
                    {}
                )
            )

            if local_names:

                crop_lines.append(
                    "Chichewa name: "
                    + str(
                        local_names.get(
                            "chichewa",
                            "Unknown"
                        )
                    )
                )

            crop_lines.append(
                "Category: "
                + str(
                    crop_information.get(
                        "category",
                        "Unknown"
                    )
                )
            )

            crop_lines.append(
                "Planting window: "
                + str(
                    crop_information.get(
                        "planting_window",
                        "Not available"
                    )
                )
            )

            crop_lines.append(
                "Rainfall requirement: "
                + str(
                    crop_information.get(
                        "rainfall_requirement",
                        "Not available"
                    )
                )
            )

            crop_lines.append(
                "Soil requirements: "
                + str(
                    crop_information.get(
                        "soil",
                        "Not available"
                    )
                )
            )

            crop_lines.append(
                "Temperature requirements: "
                + str(
                    crop_information.get(
                        "temperature",
                        "Not available"
                    )
                )
            )

            crop_lines.append(
                "Maturity: "
                + str(
                    crop_information.get(
                        "maturity",
                        "Not available"
                    )
                )
            )

            key_advice = (
                crop_information.get(
                    "key_advice",
                    []
                )
            )

            if key_advice:

                crop_lines.append(
                    "Key agricultural advice:"
                )

                for advice in key_advice:

                    crop_lines.append(
                        "- " + str(
                            advice
                        )
                    )

            sections.append(
                "CROP INFORMATION:\n"
                + "\n".join(
                    crop_lines
                )
            )

        # ----------------------------------------------
        # FARMER PROFILE
        # ----------------------------------------------

        farmer = context.get(
            "farmer"
        )

        if farmer:

            sections.append(
                "FARMER PROFILE:\n"
                + str(
                    farmer
                )
            )

        # ----------------------------------------------
        # FINAL CONTEXT
        # ----------------------------------------------

        if not sections:

            return (
                "No specific Malawi agricultural "
                "context is available."
            )

        return "\n\n".join(
            sections
        )
