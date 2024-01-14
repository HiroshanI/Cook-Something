from sklearn.feature_extraction.text import TfidfVectorizer
import pickle 

def getIngredientEmbeddings(docs):
    
    tfidf_vectorizer = TfidfVectorizer()

    ingredients_encoded = tfidf_vectorizer.fit_transform(docs)
    feature_names = tfidf_vectorizer.get_feature_names_out()
    print(feature_names)

    with open('src/ingredients_unique.csv', "w") as f:
        f.write(','.join(feature_names))

    with open('model/tfidf_encoder.pkl', "wb") as f:
        pickle.dump(tfidf_vectorizer, f)
    with open('model/ingredients_encoded.pkl', "wb") as f:
        pickle.dump(ingredients_encoded, f)

import pandas as pd
getIngredientEmbeddings(pd.read_csv('input/recipes_preprocessed.csv')['ingredients_parsed'])
    
def getInputIngredientEmbeddings(input_ingredients):

    with open('model/tfidf_encoder.pkl', "rb") as f:
        tfidf_vectorizer = pickle.load(f)

    input_encoded = tfidf_vectorizer.transform([input_ingredients])

    return input_encoded



