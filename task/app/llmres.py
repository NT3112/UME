import os
import json
from dotenv import load_dotenv
import google.generativeai as genai
import re


load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash")

def analyze_text(query):
    prompt = f"""
    Analyze the following message: "{query}"
    Respond in JSON with two fields: "tone" and "intent".
    Use actions for "intent" such as:
    "ORDER_FOOD", "FIND_RECIPE", "ASK_HELP", "SHARE_NEWS", "SLEEP","SET_TIME","SET_REMINDER"
    Only respond with JSON in this manner {{ "tone": "Excited", "intent": "ORDER_FOOD" }}
    """

    try:
        response = model.generate_content([prompt])
        content = response.text.strip()

        print("Gemini raw output:", content)
        #adding regular expression for a gemini error which i was getting
        if content.startswith("```"):
            content = re.sub(r"^```(?:json)?\s*", "", content)
            content = re.sub(r"\s*```$", "", content)

        return json.loads(content)

    except Exception as e:
        print("Gemini error:", e)
        return {"tone": "Unknown", "intent": "Unknown"}

