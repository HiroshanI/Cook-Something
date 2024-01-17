import streamlit as st
import pandas as pd
import requests
import ast

# Helper functions

st.set_page_config(layout="centered", page_title="/ CookSomething", page_icon="😋")  # Replace with your favicon path or emoji

@st.cache_data
def get_suggestions():
    return list(pd.read_csv("src/ingredients_unique.csv"))


def recommendations_page(ingredients):
    
    with st.spinner("Give me a sec, I'm finding your recipes ..."):
        recipes = requests.get("http://127.0.0.1:5000/recipe?ingredients="+ingredients)
    
    if recipes.status_code >= 500:
        st.toast("Couldn't fetch your recipes ... not your fault 😭")
    elif recipes.status_code == 200:
        st.toast(f"Found {len(recipes.json())} recipe recommendations")

    for k, v in recipes.json().items():

        st.subheader(f"""
                    Recipe {int(k)+1}: {recipes.json()[k]['recipe'].strip()}

                    
                    """)
        # Insert containers separated into tabs:
        t1, t2, t3 = st.tabs(["Overview", "Steps to cook", "Nutritional Facts"])

        # You can also use "with" notation:
        with t1:
            
            c1, c2 = st.columns(2)
            for i in ast.literal_eval(recipes.json()[k]['ingredients']):
                c1.markdown(f"- {i}")

st.header("😋 / CookSomething")
st.subheader("Let's cook something with what you have")
st.markdown("---")


suggestions = get_suggestions()
ingredients = st.multiselect("Select your ingredients here", suggestions)

if st.button("Cook Something"):
    st.markdown("---")
    recommendations_page(' '.join(ingredients))
    



