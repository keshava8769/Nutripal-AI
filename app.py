import streamlit as st
from components import meal_gen, explain_food, translator, pdf_parser
import base64

st.set_page_config(
    page_title="NutriPal AI - Your Nutrition Assistant",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Convert local image to base64 to embed inline
def image_to_base64(path):
    with open(path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

logo_base64 = image_to_base64("assets/logo.png")

# Display logo and title side by side
st.markdown(
    f"""
    <div style='display: flex; align-items: center; gap: 20px;'>
        <img src='data:image/png;base64,{logo_base64}' width='150'>
         <h1 style='margin: 0; white-space: nowrap;'> NutriPal AI - Your Nutrition Assistant</h1>
    </div>
    """,
    unsafe_allow_html=True
)


page = st.sidebar.radio("Choose a feature", [
    "Meal Recommendation",
    "Food Explainer",
    "Translate Nutrition Info",
    "Upload Nutrition PDF"
])

if page == "Meal Recommendation":
    meal_gen.generate_meal_suggestion()
elif page == "Food Explainer":
    explain_food.explain_nutrition_item()
elif page == "Translate Nutrition Info":
    translator.translate_advice()
elif page == "Upload Nutrition PDF":
    pdf_parser.parse_pdf()
