# CookSomething 

## Contents
1. Overview
1. Setup
1. Files
1. Technologies
1. Demo

## 1. Overview
Welcome to CookSomething 😋! This Python-based web application is designed to reccomend recipes based on ingredients a user might have. This tool is perfect for anyone interested in cooking but doesn't have time going through recipes or the grocery 😉.

> This Project is submitted as a final project for __CS50's Introduction to Python Programming Course__

## 2. Setup
1. Install all requirements
`pip install -r requirements.txt`
2. Run Backend
`python app.py`
3. Run Frontend
`streamlit run frontend/app.py`

## 3. Files
📂 Frontend 
- app.py : Frontend code (Streamlit)
---
📂 Input
- recipes_preprocessed.csv : Contains more than 4000 recipes preprocessed
- recipes_scraped.csv : Contains recipes in the scraped format
---
📂 Model
- ingredients_encoded.pkl : Contains encoded ingredients in binary format
- tfidf_encoder.pkl : Trained TFIDF Vectorizer with encoded ingredients
---
📂 src
- common_words.csv : Contains common words used by cooking websites
- ingredients_unique.csv : Contains unique ingredients from all the recipes
---
- app.py : Flask-based backend 
- embedding : Encoding ingredients
- preprocess.py : Preprocess the scraped recipes
- recommender.py : Recommendation system
---
- requirements.txt : Libraries and Modules used to make this app work 

## 4. Technologies
- Python
- NLTK
- Streamlit
- Flask
- Cosine-Similarity
- HTML
- Markdown

## 5. Demo
![Screenshot of the Streamlit Application](src/screenshot.png)
Video Demo : [Click here to go to Youtube](https://youtu.be/Mph68kY09WU)



