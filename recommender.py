import pandas as pd
import pickle
from sklearn.metrics.pairwise import cosine_similarity
from preprocess import parseIngredients

from embedding import getInputIngredientEmbeddings

def getScores(input_ingredients):

    input_ingredients_preprocessed = parseIngredients(input_ingredients)
    input_encoded = getInputIngredientEmbeddings(input_ingredients_preprocessed)
    
    with open("model/ingredients_encoded.pkl", 'rb') as f:
        docs_vec = pickle.load(f)        

    cos_sim_scores = map(lambda doc: cosine_similarity(input_encoded, doc)[0][0], docs_vec)
    return list(cos_sim_scores)


def getRecommendations(N, scores):
    
    print("getting recs") 
    recipes = pd.read_csv("./input/recipes_preprocessed.csv")

    top_recipes_idx = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:N]
    top_recipes_scores = sorted(scores, reverse=True)[:N]

    top_recipes = recipes.loc[top_recipes_idx, :]
    top_recipes['scores'] = top_recipes_scores
    
    return top_recipes
    

def getRecipeRecommendations(N, input_ingredients):
    scores = getScores(input_ingredients)
    return getRecommendations(N, scores)


# print(getRecipeRecommendations(5, ["ground beef, pasta, spaghetti, tomato pasta sauce, bacon, onion, zucchini, and, cheese"])[['recipe_name', 'scores']])
