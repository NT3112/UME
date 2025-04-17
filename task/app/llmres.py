import os
import json
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key from .env
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize Gemini model
model = genai.GenerativeModel("gemini-pro")

def analyze_text(query):
    prompt = f"""
    Analyze the following message: "{query}"
    Respond in JSON with two fields: "tone" and "intent".
    Use actions for "intent" such as:
    "ORDER_FOOD", "FIND_RECIPE", "ASK_HELP", "SHARE_NEWS", "SLEEP"
    Only respond with JSON.
    Example: {{ "tone": "Excited", "intent": "ORDER_FOOD" }}
    """

    try:
        # 👇 THIS IS THE KEY LINE
        response = model.generate_content([prompt])
        content = response.text.strip()
        print("Gemini raw output:", content)
        return json.loads(content)

    except Exception as e:
        print("Gemini error:", e)
        return {"tone": "Unknown", "intent": "Unknown"}
