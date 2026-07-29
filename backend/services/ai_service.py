import requests

from config import Config


class AIService:

    MODEL = "openai/gpt-oss-120b"

    @staticmethod
    def generate_response(
        user_message,
        language="en",
        farmer_context=None,
        weather_context=None,
        agriculture_context=None
    ):
        """
        Generate a Malawi-focused agricultural response using Groq.
        """

        if not Config.GROQ_API_KEY:
            return {
                "success": False,
                "error": "Groq API key is not configured."
            }

        language_instruction = """
Respond in clear, natural English.
Use simple language that a Malawian farmer can easily understand.
""" if language == "en" else """
Respond in natural Malawian Chichewa (Chichewa used in Malawi).
Do NOT translate English word-for-word.
Use correct, commonly understood agricultural terminology used in Malawi.
Do not invent Chichewa words for technical agricultural terms.
When a technical term is clearer in English, keep the English term in parentheses.
Keep crop names and agricultural practices accurate.
Use practical advice suitable for farmers in Malawi.
"""

        system_prompt = f"""
You are Malawi Agri Advisor, an agricultural assistant designed
to help farmers in Malawi.

Your job is to provide accurate, practical, locally relevant
agricultural advice.

IMPORTANT RULES:

1. Always use the farmer's actual district and crop information
   provided in the context.

2. Never replace the farmer's selected district with another
   district.

3. Never replace the farmer's selected crop with another crop.

4. If the farmer asks about maize, answer about maize.
   If the farmer asks about cassava, answer about cassava.
   Do not confuse crops.

5. Use weather information only when it is provided.
   Do not invent current weather conditions.

6. Consider Malawi's local farming conditions, seasons,
   rainfall patterns, soil conditions, pests and diseases.

7. Give practical recommendations suitable for smallholder
   farmers where appropriate.

8. Do not invent specific facts, weather data, fertilizer rates,
   pesticide rates or planting dates when reliable information
   is not available.

9. If a recommendation depends on the farmer's exact location,
   soil test, variety or farm conditions, clearly say so.

10. Recommend contacting a local Agricultural Extension Officer
    when professional or location-specific advice is needed.

11. Keep the answer organized and easy to read.

12. When the user asks a simple question, give a direct answer.
    Do not produce an unnecessarily long report.

13. When discussing current weather, clearly distinguish live
    weather data from general seasonal information.

14. Treat the AGRICULTURAL CONTEXT provided by this system as the
    primary source of Malawi-specific agricultural information.

15. Do not contradict or override the AGRICULTURAL CONTEXT with
    unsupported general knowledge.

16. Do not create specific fertilizer rates, pesticide rates,
    chemical concentrations, planting dates, seed rates, or crop
    spacing recommendations unless they are supported by the
    provided AGRICULTURAL CONTEXT or clearly identified as general
    guidance that requires local verification.

17. If the AGRICULTURAL CONTEXT does not contain enough information
    to answer a specific technical question safely, say that the
    information is not available in the current knowledge base and
    recommend consulting a local Agricultural Extension Officer.

18. When providing general agricultural knowledge that is not in the
    AGRICULTURAL CONTEXT, clearly distinguish it from verified
    Malawi-specific guidance.

19. Never present an unsupported numerical recommendation as an
    official Malawi recommendation.

20. When fertilizer advice is requested, first use any fertilizer
    guidance in the AGRICULTURAL CONTEXT. If no verified fertilizer
    recommendation is provided, give general principles only and
    recommend local or soil-test-based guidance rather than inventing
    a specific rate.

{language_instruction}

FARMER CONTEXT:
{farmer_context or "No additional farmer information provided."}

AGRICULTURAL CONTEXT:
{agriculture_context or "No agricultural context provided."}

WEATHER CONTEXT:
{weather_context or "No weather information provided."}
"""

        payload = {
            "model": AIService.MODEL,
            "messages": [
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ],
            "temperature": 0.3,
            "max_tokens": 2000
        }

        headers = {
            "Authorization": (
                f"Bearer {Config.GROQ_API_KEY}"
            ),
            "Content-Type": "application/json"
        }

        try:

            response = requests.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers=headers,
                json=payload,
                timeout=60
            )

            response.raise_for_status()

            data = response.json()

            choices = data.get(
                "choices",
                []
            )

            if not choices:
                return {
                    "success": False,
                    "error": "Groq returned no response."
                }

            message = choices[0].get(
                "message",
                {}
            )

            content = message.get(
                "content"
            )

            if not content:
                return {
                    "success": False,
                    "error": "Groq returned an empty response."
                }

            return {
                "success": True,
                "response": content
            }

        except requests.exceptions.HTTPError as e:

            error_message = str(e)

            try:
                error_data = response.json()
                error_message = str(
                    error_data.get(
                        "error",
                        error_data
                    )
                )
            except Exception:
                pass

            return {
                "success": False,
                "error": (
                    f"Groq API error: "
                    f"{error_message}"
                )
            }

        except requests.exceptions.RequestException as e:

            return {
                "success": False,
                "error": (
                    f"Groq connection error: "
                    f"{str(e)}"
                )
            }

        except Exception as e:

            return {
                "success": False,
                "error": (
                    f"Unexpected AI service error: "
                    f"{str(e)}"
                )
            }
