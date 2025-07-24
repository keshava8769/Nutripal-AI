import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load Gemini API Key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")

def explain_nutrition_item():
    item = st.text_input("Enter a food item (e.g., broccoli):")
    if st.button("Explain"):
        try:
            # Load and format the prompt
            prompt_template = open("prompts/food_explainer.txt").read()
            prompt = prompt_template.format(food_item=item)

            with st.spinner("Explaining nutritional benefits..."):
                response = model.generate_content(prompt)
                st.success("Here's the explanation:")
                st.write(response.text)
        except Exception as e:
            st.error(f"Failed to generate explanation: {e}")
