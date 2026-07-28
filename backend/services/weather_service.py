import requests

from config import Config


class WeatherService:
    """
    Weather service for Malawi Agri Advisor.

    Uses OpenWeather to retrieve current weather
    conditions for a farmer's location.
    """

    BASE_URL = (
        "https://api.openweathermap.org/data/2.5/weather"
    )

    @staticmethod
    def get_current_weather(
        latitude,
        longitude
    ):
        """
        Get current weather from OpenWeather.
        """

        if not Config.OPENWEATHER_API_KEY:
            return {
                "success": False,
                "error": (
                    "OpenWeather API key "
                    "is not configured."
                )
            }

        params = {
            "lat": latitude,
            "lon": longitude,
            "appid": Config.OPENWEATHER_API_KEY,
            "units": "metric"
        }

        try:

            response = requests.get(
                WeatherService.BASE_URL,
                params=params,
                timeout=15
            )

            response.raise_for_status()

            data = response.json()

            main = data.get(
                "main",
                {}
            )

            wind = data.get(
                "wind",
                {}
            )

            weather_list = data.get(
                "weather",
                []
            )

            weather = (
                weather_list[0]
                if weather_list
                else {}
            )

            rain = data.get(
                "rain",
                {}
            )

            result = {
                "success": True,

                "location": {
                    "name": data.get(
                        "name"
                    ),
                    "latitude": latitude,
                    "longitude": longitude
                },

                "temperature": {
                    "current_celsius": main.get(
                        "temp"
                    ),
                    "feels_like_celsius": main.get(
                        "feels_like"
                    ),
                    "min_celsius": main.get(
                        "temp_min"
                    ),
                    "max_celsius": main.get(
                        "temp_max"
                    )
                },

                "humidity_percent": main.get(
                    "humidity"
                ),

                "pressure_hpa": main.get(
                    "pressure"
                ),

                "conditions": {
                    "main": weather.get(
                        "main"
                    ),
                    "description": weather.get(
                        "description"
                    )
                },

                "wind": {
                    "speed_mps": wind.get(
                        "speed"
                    ),
                    "direction_degrees": wind.get(
                        "deg"
                    )
                },

                "rain": {
                    "last_hour_mm": rain.get(
                        "1h",
                        0
                    ),
                    "last_3_hours_mm": rain.get(
                        "3h",
                        0
                    )
                }
            }

            return result

        except requests.exceptions.Timeout:

            return {
                "success": False,
                "error": (
                    "OpenWeather request timed out."
                )
            }

        except requests.exceptions.HTTPError:

            try:
                error_data = response.json()
            except Exception:
                error_data = response.text

            return {
                "success": False,
                "error": (
                    "OpenWeather API error: "
                    + str(error_data)
                )
            }

        except requests.exceptions.RequestException as error:

            return {
                "success": False,
                "error": (
                    "Weather connection error: "
                    + str(error)
                )
            }

        except Exception as error:

            return {
                "success": False,
                "error": (
                    "Unexpected weather error: "
                    + str(error)
                )
            }


    @staticmethod
    def format_for_ai(
        weather_data
    ):
        """
        Convert weather data into a clean,
        AI-readable agricultural weather context.
        """

        if not weather_data:

            return (
                "No weather information "
                "is currently available."
            )

        if not weather_data.get(
            "success"
        ):

            return (
                "Weather information could "
                "not be retrieved."
            )

        location = weather_data.get(
            "location",
            {}
        )

        temperature = weather_data.get(
            "temperature",
            {}
        )

        conditions = weather_data.get(
            "conditions",
            {}
        )

        wind = weather_data.get(
            "wind",
            {}
        )

        rain = weather_data.get(
            "rain",
            {}
        )

        return f"""
CURRENT WEATHER CONTEXT:

Location:
{location.get("name", "Unknown")}

Temperature:
{temperature.get("current_celsius", "Unknown")} °C

Feels like:
{temperature.get("feels_like_celsius", "Unknown")} °C

Minimum temperature:
{temperature.get("min_celsius", "Unknown")} °C

Maximum temperature:
{temperature.get("max_celsius", "Unknown")} °C

Humidity:
{weather_data.get("humidity_percent", "Unknown")} %

Conditions:
{conditions.get("description", "Unknown")}

Wind speed:
{wind.get("speed_mps", "Unknown")} m/s

Rainfall in last hour:
{rain.get("last_hour_mm", 0)} mm

Rainfall in last 3 hours:
{rain.get("last_3_hours_mm", 0)} mm
""".strip()
