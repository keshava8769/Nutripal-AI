import streamlit as st
import fitz  # PyMuPDF
from io import BytesIO
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load Gemini API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def parse_pdf():
    st.subheader("📄 Upload a Nutrition Label PDF")
    uploaded_file = st.file_uploader("Upload PDF file", type=["pdf"])

    if uploaded_file is not None:
        try:
            # Wrap uploaded file bytes into a BytesIO stream
            file_bytes = uploaded_file.read()
            pdf_stream = BytesIO(file_bytes)

            # Use PyMuPDF to open the PDF stream
            with fitz.open(stream=pdf_stream, filetype="pdf") as doc:
                extracted_text = ""
                for page in doc:
                    extracted_text += page.get_text()

            if not extracted_text.strip():
                st.warning("⚠️ No text found in the uploaded PDF.")
                return

            # Load the prompt template and format it
            with open("prompts/nutrition_summary.txt", "r") as f:
                prompt_template = f.read()
            prompt = prompt_template.format(content=extracted_text)

            # Send to Gemini for analysis
            with st.spinner("🔍 Summarizing nutrition data..."):
                response = model.generate_content(prompt)
                st.success("Nutrition Summary:")
                st.write(response.text)

        except Exception as e:
            st.error(f"❌ Error reading PDF: {str(e)}")
