import streamlit as st
import pandas as pd
import requests

@st.cache_data
def getIngredients():
    return pd.read_csv("src/ingredients_unique.csv")

# Set the page title and favicon
st.set_page_config(page_title="Cook Something", page_icon="🥪", layout="centered")

# Set the background color
st.markdown(
    """
    <style>
        body {
            background-color: white;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Set the title and subtitle
st.title("Aesthetic Streamlit App")
st.subheader("Enter some text and click the Submit button")

# Add a text input widget
suggestions = list(getIngredients())

ingredients = st.multiselect("Select your ingredients", options=suggestions, key="selected_ingreds")

# Add a submit button
if st.button("Submit"):
    # Display the input text
    ingredients=' '.join(ingredients)
    print(ingredients)
    top_recipes = requests.get("https://coook-something-recipe-recommender.onrender.com/recipe?ingredients="+ingredients)
    print(top_recipes)  
