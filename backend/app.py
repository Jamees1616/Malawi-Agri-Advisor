from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

from config import Config
from services.weather_service import WeatherService
from services.ai_service import AIService
from services.context_service import ContextService

from data.malawi_agriculture import (
    MALAWI_REGIONS,
    CROPS,
    GENERAL_FARMING_GUIDANCE,
    get_all_districts,
    get_region_by_district,
    get_crop
)


def create_app():
    app = Flask(
        __name__,
        static_folder="static",
        static_url_path="/static"
    )

    app.config.from_object(Config)
    CORS(app)

    @app.route("/", methods=["GET"])
    def home():
        return send_from_directory(
            app.static_folder,
            "index.html"
        )

    @app.route("/api/health", methods=["GET"])
    def health():
        return jsonify({
            "success": True,
            "status": "healthy",
            "service": "Malawi Agri Advisor Backend"
        })

    @app.route("/api/weather/current", methods=["GET"])
    def current_weather():
        latitude = request.args.get("lat", type=float)
        longitude = request.args.get("lon", type=float)

        if latitude is None or longitude is None:
            return jsonify({
                "success": False,
                "error": "Latitude and longitude are required."
            }), 400

        if not -90 <= latitude <= 90:
            return jsonify({
                "success": False,
                "error": "Invalid latitude."
            }), 400

        if not -180 <= longitude <= 180:
            return jsonify({
                "success": False,
                "error": "Invalid longitude."
            }), 400

        result = WeatherService.get_current_weather(
            latitude,
            longitude
        )

        if not result.get("success"):
            return jsonify(result), 502

        return jsonify(result), 200

    @app.route("/api/agriculture/regions", methods=["GET"])
    def get_regions():
        return jsonify({
            "success": True,
            "regions": MALAWI_REGIONS
        })

    @app.route("/api/agriculture/districts", methods=["GET"])
    def get_districts():
        districts = get_all_districts()

        return jsonify({
            "success": True,
            "count": len(districts),
            "districts": districts
        })

    @app.route(
        "/api/agriculture/district/<district_name>",
        methods=["GET"]
    )
    def get_district_information(district_name):
        region = get_region_by_district(district_name)

        if region is None:
            return jsonify({
                "success": False,
                "error": "District not found."
            }), 404

        return jsonify({
            "success": True,
            "district": district_name,
            "region": region
        })

    @app.route("/api/agriculture/crops", methods=["GET"])
    def get_crops():
        crop_list = []

        for crop_id, crop_data in CROPS.items():
            crop_list.append({
                "id": crop_id,
                "name": crop_data["name"],
                "category": crop_data["category"],
                "local_name": crop_data["local_names"].get(
                    "chichewa"
                )
            })

        return jsonify({
            "success": True,
            "count": len(crop_list),
            "crops": crop_list
        })

    @app.route(
        "/api/agriculture/crop/<crop_name>",
        methods=["GET"]
    )
    def get_crop_information(crop_name):
        crop = get_crop(crop_name)

        if crop is None:
            return jsonify({
                "success": False,
                "error": "Crop not found."
            }), 404

        return jsonify({
            "success": True,
            "crop": crop
        })

    @app.route(
        "/api/agriculture/guidance",
        methods=["GET"]
    )
    def get_farming_guidance():
        return jsonify({
            "success": True,
            "guidance": GENERAL_FARMING_GUIDANCE
        })

    @app.route(
        "/api/agriculture/context",
        methods=["POST"]
    )
    def build_agricultural_context():
        data = request.get_json(silent=True)

        if not data:
            return jsonify({
                "success": False,
                "error": "Request body must contain JSON data."
            }), 400

        district = data.get("district")
        crop = data.get("crop")
        farmer_context = data.get("farmer_context")

        context = ContextService.build_context(
            district=district,
            crop=crop,
            farmer_context=farmer_context
        )

        formatted_context = ContextService.format_for_ai(
            context
        )

        return jsonify({
            "success": True,
            "context": context,
            "formatted_context": formatted_context
        })

    @app.route("/api/chat", methods=["POST"])
    def chat():
        data = request.get_json(silent=True)

        if not data:
            return jsonify({
                "success": False,
                "error": "Request body must contain JSON data."
            }), 400

        user_message = data.get("message")

        if not user_message:
            return jsonify({
                "success": False,
                "error": "The 'message' field is required."
            }), 400

        language = data.get("language", "en")
        district = data.get("district")
        crop = data.get("crop")
        farmer_context = data.get("farmer_context")

        context = ContextService.build_context(
            district=district,
            crop=crop,
            farmer_context=farmer_context
        )

        agriculture_context = ContextService.format_for_ai(
            context
        )

        location = context.get("location", {})

        latitude = location.get("latitude")
        longitude = location.get("longitude")

        weather_data = None

        weather_context = (
            "CURRENT WEATHER CONTEXT:\n"
            "Live weather data is not available."
        )

        if latitude is not None and longitude is not None:
            weather_data = WeatherService.get_current_weather(
                latitude,
                longitude
            )

            if weather_data.get("success"):
                if hasattr(
                    WeatherService,
                    "format_for_ai"
                ):
                    weather_context = (
                        WeatherService.format_for_ai(
                            weather_data
                        )
                    )
                else:
                    weather_context = str(
                        weather_data
                    )

        result = AIService.generate_response(
            user_message=user_message,
            language=language,
            farmer_context=farmer_context,
            weather_context=weather_context,
            agriculture_context=agriculture_context
        )

        if not result.get("success"):
            return jsonify(result), 502

        return jsonify({
            "success": True,
            "response": result["response"],
            "context": {
                "district": district,
                "crop": crop,
                "location": location,
                "weather": weather_data
            }
        })

    return app


app = create_app()


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
