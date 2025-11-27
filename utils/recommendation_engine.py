import os
import google.generativeai as genai
from dotenv import load_dotenv
import streamlit as st

# Load .env if running locally (optional helper)
load_dotenv()

# Prefer Streamlit secrets; fallback to environment variable if needed
API_KEY = st.secrets.get("API_KEY") or os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("❌ Gemini API key not found. Set it in st.secrets or as environment variable 'API_KEY'.")

genai.configure(api_key=API_KEY)

def generate_recommendations(user_data: dict, confirmed_conditions: list[str]) -> str:
    conditions_md = "\n".join(f"- {cond}" for cond in confirmed_conditions) if confirmed_conditions else "None specified"

    prompt = f"""
    You are a health assistant. Generate a personalized wellness plan with:

    ### 👤 User Summary
    Name: {user_data.get("name")}
    Age: {user_data.get("age")}
    Goal: {user_data.get("goal")}

    ### 🧠 Confirmed Health Conditions
    {conditions_md}

    ### 🍽️ Food Plan
    - Foods to eat (with reasoning)
    - Foods to avoid

    ### 🏃 Exercise Plan
    - Weekly plan based on goal & conditions

    ### 💊 Supplement Suggestions
    - If any deficiencies apply
    """

    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt)
    return response.text
