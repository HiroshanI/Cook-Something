import streamlit as st
import pandas as pd
import requests
import ast
from tabulate import tabulate
@st.cache_data
def getIngredients():
    return pd.read_csv("src/ingredients_unique.csv")

def getRecommendations(ingredients):
    return requests.get("http://127.0.0.1:5000/recipe?ingredients="+ingredients).json()

# Set the page title and favicon
st.set_page_config(page_title="Cook Something", page_icon="🍕", layout="centered")

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
st.title("🍜 Cook Something!")
st.subheader("Select some ingredients and let's get cooking ...")

# Add a text input widget
suggestions = list(getIngredients())

ingredients = st.multiselect("Select your ingredients", options=suggestions, key="selected_ingreds")

# Add a submit button
if st.button("Submit", key='recommend'):
    # Display the input text
    ingredients=' '.join(ingredients)
    print(ingredients)
    # top_recipes = requests.get("https://coook-something-recipe-recommender.onrender.com/recipe?ingredients="+ingredients).json()
    top_recipes = getRecommendations(ingredients)
    
    for i in range(1):
        st.markdown("## **" + top_recipes[str(i)]['recipe'] + "**")

        for ingredient in ast.literal_eval(top_recipes[str(i)]['ingredients']):
            st.markdown('- '+ingredient)
        
        st.markdown('**URL**: ' + top_recipes[str(i)]['url'])

