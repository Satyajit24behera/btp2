import os
import google.generativeai as genai
from dotenv import load_dotenv
import streamlit as st
load_dotenv()
genai.configure(api_key="AIzaSyA7ccHU1oXGCynowICckB4lYZ3ZLf5GxYk")

def match_conditions(user_data: dict, medical_report: str = "") -> str:
    prompt = f"""
    Analyze the user's data and suggest possible underlying health conditions in a structured format:

    ### 🧠 Possible Health Conditions
    - Condition 1
    - Condition 2
    - ...

    User Data:
    {user_data}

    Medical Report:
    {medical_report if medical_report else 'Not provided'}
    """
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text
