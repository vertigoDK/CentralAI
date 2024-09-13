import os
import google.generativeai as genai
from dotenv import load_dotenv

class GeminiAI:
    def __init__(self):
        genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

        self._model = genai.GenerativeModel("gemini-1.5-flash")

