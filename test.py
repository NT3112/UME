import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

for model in genai.list_models():
    print(f"Model: {model.name}")
    for method in model.supported_generation_methods:
        print(f"- Supports: {method}")