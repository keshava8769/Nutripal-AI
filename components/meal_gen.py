import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Gemini API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")

def generate_meal_suggestion():
    goal = st.text_input("Enter your health goal (e.g., weight loss):")
    diet = st.text_input("Diet preferences (e.g., veg, low-carb):")

    if st.button("Generate Meal Plan"):
        if not goal or not diet:
            st.warning("Please fill in both fields.")
            return

        prompt = f"You are a helpful nutrition assistant. Suggest a nutritious {diet} meal plan for someone whose goal is {goal}."

        try:
            response = model.generate_content(prompt)
            st.success("Here's your recommended meal plan:")
            st.write(response.text)

        except Exception as e:
            st.error(f"Error: {e}")
