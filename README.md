# 🥗 NutriPal AI - Your Nutrition Assistant

NutriPal AI is an intelligent nutrition assistant built using **Streamlit** and powered by **Gemini AI** (Google Generative AI). It helps users make better food decisions through personalized meal recommendations, nutritional explanations, multilingual translations, and PDF-based nutrition parsing.

---

## 🚀 Features

- ✅ **Meal Recommendation**  
  Generate healthy meal suggestions using Gemini AI based on nutritional goals.

- ✅ **Food Explainer**  
  Enter any food item and get a detailed explanation of its nutritional benefits.

- ✅ **Translate Nutrition Info**  
  Translate dietary advice into regional Indian languages like Hindi, Telugu, Tamil, and Kannada.

- ✅ **PDF Parsing**  
  Upload nutrition PDF documents and extract readable, structured content with Gemini.

---

## 🧠 Built With

- [Streamlit](https://streamlit.io/) – Fast Python framework for building web apps
- [Google Generative AI (Gemini)](https://ai.google.dev/) – Language model for text generation
- [Python](https://www.python.org/) – Core programming language
- [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/) – For parsing PDF files
- [dotenv](https://pypi.org/project/python-dotenv/) – Manage API keys securely

---

## 📦 Project Structure

NutriPal-AI/
│
├── app.py # Main Streamlit app
├── assets/
│ └── logo.png # Logo used in the UI
├── prompts/
│ ├── food_explainer.txt # Prompt template for food explanation
│ └── translate.txt # Prompt template for translations
├── components/
│ ├── meal_gen.py # Gemini-powered meal suggestion logic
│ ├── explain_food.py # Explains nutritional value of food items
│ ├── translator.py # Language translation component
│ └── pdf_parser.py # PDF upload and parsing logic
├── .env # Store your Gemini API key securely
├── requirements.txt # Python dependencies
└── README.md # Project documentation



## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Nutripal-AI.git
   cd Nutripal-AI
