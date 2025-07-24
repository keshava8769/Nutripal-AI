import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize Gemini model
model = genai.GenerativeModel(model_name="gemini-2.5-flash")

def translate_advice():
    st.subheader("🌐 Translate Nutrition Advice")

    advice = st.text_area("Enter nutrition advice to translate:")
    lang = st.selectbox("Choose target language", ["Hindi", "Telugu", "Tamil", "Kannada"])

    if st.button("Translate"):
        if not advice.strip():
            st.warning("⚠️ Please enter some advice text.")
            return

        try:
            # Load and format prompt template
            with open("prompts/translate.txt", "r", encoding="utf-8") as f:
                prompt_template = f.read()
        except FileNotFoundError:
            st.error("❌ Prompt file not found at `prompts/translate.txt`. Please create one.")
            return

        prompt = prompt_template.format(advice=advice, language=lang)

        with st.spinner("Translating..."):
            try:
                response = model.generate_content(prompt)
                st.success(f"✅ Translated into {lang}:")
                st.write(response.text)
            except Exception as e:
                st.error(f"❌ Translation failed: {e}")
