# Imports 
import pandas as pd
import string
import ast
import re
from unidecode import unidecode
import nltk
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer

def parseIngredients(ingredients, 
                     translator=str.maketrans("", "", string.punctuation), 
                     lemmatizer=WordNetLemmatizer(), 
                     common_words=list(pd.read_csv('src/common_words.csv'))):

    """
    Extract and pre-process the ingredients

    :params
    - ingredients (string): Ingredients for a recipe imported from CSV file

    :return
    - ingredient_list (string): List of ingredients for the recipe 
                                separated by spaces, None if empty
    """

    ingredient_list = list() # Output variable
    
    # Extract ingredients list from recipes
    if not isinstance(ingredients, list):
        print(ingredients)
        ingredients = ast.literal_eval(ingredients)

    # Lemmatize common words
    common_lemmas = [lemmatizer.lemmatize(word.lower()) \
                     for word in common_words] 
    
    for ingredient in ingredients:
        
        # Remove punctuations
        ingredient = ingredient.translate(translator) 

        # Extract lemmatized tokens from each ingredient 
        tokens = [lemmatizer.lemmatize(unidecode(token.lower().strip())) \
                  for token in re.split(' |-', ingredient) 
                      if token.isalpha()] 
        
        # Remove common lemmas (tokens)
        lemmas = [token for token in tokens
                      if token not in common_lemmas]

        # Create a list of lemmas
        ingredient_list.extend(lemmas)

    # Sort ingredients if it is not empty
    ingredient_list = ' '.join(sorted(ingredient_list)) \
                            if len(ingredient_list) > 0 \
                            else None
    return ingredient_list

def parseNames(names):
    
    """
    Preprocess the names of the recipes
    
    :params
    - names (list): Recipe names
    
    :return 
    - new_names (list): Fixed recipe names
    """

    new_names = list()

    for name in names:
        if name.endswith("Recipe - Allrecipes.com"):
            new_names.append(name.replace(" Recipe - Allrecipes.com", ""))
        else:
            new_names.append(name)

def preprocess_recipes(filepath):

    common_words = list(pd.read_csv('src/common_words.csv'))
    translator = str.maketrans("", "", string.punctuation) 
    lemmatizer = WordNetLemmatizer()
    
    # Read file
    recipes_df = pd.read_csv(filepath)

    # Add parsed ingredients into recipes data
    recipes_df['ingredients_'] = [parseIngredients(ingredients, 
                                                         translator, lemmatizer, common_words) 
                                                         for ingredients in recipes_df['ingredients']]

    # Drop null data
    recipes_preprocessed = recipes_df.dropna(axis=0)

    # Fix recipe names
    recipes_preprocessed['recipe_name'] = parseNames(recipes_preprocessed['recipe_name'])

    # Create new CSV file 
    recipes_preprocessed.to_csv("input/recipes_preprocessed.csv", index=False)
    print("\nCreated file: input/recipes_preprocessed.csv\n")

    return recipes_preprocessed

def get_ingredients_list(ingredients):
    return list(ingredients)

