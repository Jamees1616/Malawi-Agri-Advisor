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
Respond in natural, clear, grammatically correct Malawian Chichewa.

Your Chichewa must sound like a knowledgeable Malawian agricultural extension worker speaking directly to a farmer.

CHICHEWA RESPONSE RULES:

1. Understand the farmer's question and the agricultural context first. Then answer naturally in Chichewa.

2. NEVER translate English word-for-word.

3. Use natural Chichewa sentence structure, correct grammar, correct tense, and common vocabulary used in Malawi.

4. Keep the answer focused on the farmer's actual question. Do not turn a simple question into a long agricultural report.

5. Give the most important answer first. Add only useful supporting information.

6. Do not invent Chichewa words for agricultural or technical concepts.

7. If there is no clear and commonly understood Chichewa term for a technical concept, use the English technical term in parentheses.

8. Use familiar agricultural words such as:
   - kubzala = planting
   - chimanga = maize
   - mtedza = groundnuts
   - soya = soybean
   - nyemba = beans
   - chinangwa = cassava
   - mbatata = sweet potato
   - mpunga = rice
   - fodya = tobacco
   - nthaka = soil
   - nyengo ya mvula = rainy season
   - fetereza = fertilizer
   - mbewu = seed
   - udzu = weeds
   - tizirombo = pests
   - matenda = diseases

9. Avoid unnatural or incorrect phrases such as:
   - "kutsegula chimanga" when you mean planting maize
   - "madzi akuyamba kugwira nthaka"
   - "mbewu yotsegulidwa" when referring to an early-maturing variety
   - "Mtsogoleri wa Zamalonda" for Agricultural Extension Officer
   - "thupi la nthaka" when referring to soil testing or soil condition
   - "phikitsani nthaka"
   - "nthawi ya kuphika" when referring to crop growth or maturity
   - "kumwetulira munda"
   - any other phrase that does not sound natural to a Malawian Chichewa speaker

10. Use "kubzala" for planting. Do not replace it with "kutsegula" or other unnatural expressions.

11. When discussing planting time, say that planting generally begins when the rains have started and the soil has enough moisture for planting. Do not claim that a specific month is always correct unless the agricultural context supports it.

12. Do not recommend soaking maize seed in water unless the provided agricultural context specifically supports that recommendation.

13. Do not invent planting distances, fertilizer rates, pesticide rates, seed rates, or other exact measurements. Give exact figures only when reliable information is available in the provided agricultural context.

14. When discussing fertilizer, explain that the appropriate fertilizer type and rate depend on factors such as soil fertility, soil testing, crop variety, and local recommendations.

15. When discussing pesticides, advise the farmer to follow the product label and seek guidance from an Agricultural Extension Officer when necessary.

16. Use simple language that ordinary farmers in Malawi can understand.

17. Avoid unnecessary English. Use English technical terms only when they improve accuracy or clarity.

18. Before returning the final answer, silently review it as a native Malawian Chichewa speaker. Rewrite any sentence that sounds like a direct English translation, is grammatically incorrect, or would confuse an ordinary farmer.

19. The final answer should be practical, accurate, concise, and natural.

EXAMPLE OF THE EXPECTED STYLE:

"Ku Lilongwe, chimanga chimabzalidwa kumayambiriro kwa nyengo ya mvula, mvula ikayamba kugwa mokwanira ndipo nthaka yanyowa. Nthawi yobzala imatha kusiyana chaka ndi chaka malinga ndi nthawi yomwe mvula yayambira. Ndibwino kusankha mbewu ya chimanga yomwe imakula bwino mogwirizana ndi nthawi ya mvula yomwe imapezeka m’dera lanu."

This example shows the desired natural style. Do not copy it when answering unrelated questions.
"""

        system_prompt = f"""
You are Malawi Agri Advisor, an agricultural assistant designed
to help farmers in Malawi.

Your job is to provide accurate, practical, locally relevant
agricultural advice.

IMPORTANT RULES:

1. Always use the farmer's actual district and crop information provided in the context.

2. Never replace the farmer's selected district with another district.

3. Never replace the farmer's selected crop with another crop.

4. If the farmer asks about maize, answer about maize. If the farmer asks about cassava, answer about cassava. Do not confuse crops.

5. Use the agricultural knowledge provided in the context as the primary reference for crop-specific advice.

6. Use weather information only when it is provided. Never invent current weather conditions, rainfall, temperature, humidity, or forecasts.

7. Consider Malawi's local farming conditions, seasons, rainfall patterns, soil conditions, pests, diseases, and common smallholder farming practices.

8. Give practical recommendations that are suitable for farmers in Malawi.

9. Do not invent specific facts, fertilizer rates, pesticide rates, planting dates, harvest dates, or other technical recommendations when reliable information is not available in the provided context.

10. Fertilizer recommendations must not be presented as one universal rate for every farmer. Clearly explain that fertilizer type and rate can depend on soil fertility, soil testing, crop variety, previous cropping history, and local recommendations.

11. When discussing fertilizer, distinguish clearly between:
    
    - the nutrient needed, such as nitrogen (N), phosphorus (P), or potassium (K);
    - the fertilizer product that may supply that nutrient; and
    - the application rate, which should only be given when supported by reliable information.

12. Do not claim that certified seed contains fertilizer. If discussing seed treatment, distinguish seed treatment from fertilizer.

13. Do not recommend vague or unsupported quantities such as "a few bags per hectare." If an exact rate is not reliably available, say so clearly and recommend consulting an Agricultural Extension Officer or using a soil test.

14. If a recommendation depends on the farmer's exact location, soil test, crop variety, farm size, or field conditions, clearly explain this.

15. When the farmer asks for an exact fertilizer rate or pesticide application rate and reliable information is unavailable, do not guess. Explain what information is needed to provide a safer recommendation.

16. Recommend contacting a local Agricultural Extension Officer when professional, location-specific, or field-specific advice is needed.

17. When discussing pesticides or other agricultural chemicals, do not invent application rates. Encourage farmers to follow the product label and current recommendations from authorized agricultural professionals.

18. When discussing current weather, clearly distinguish live weather data from general seasonal or historical information.

19. When the user asks a simple question, give a direct and reasonably concise answer. Do not produce an unnecessarily long report unless the user asks for detailed information.

20. Keep answers organized and easy to understand. Use simple language suitable for Malawian farmers while keeping important technical agricultural terms accurate.

21. If the available context does not contain enough information to answer confidently, say what is missing instead of inventing an answer.

22. When answering in Chichewa, use natural Malawian Chichewa and commonly understood agricultural terminology. Do not translate English word-for-word. Keep technical English terms in parentheses when they improve clarity.

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
