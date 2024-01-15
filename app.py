from flask import Flask, jsonify, request
from recommender import getRecipeRecommendations

app = Flask(__name__)

@app.route('/', methods=["GET"])
def hello():
    HELLO_HTML = """
     <html><body>
         <h1>Welcome to my api: Whatscooking!</h1>
         <p>Please add some ingredients to the url to receive recipe recommendations.
            You can do this by appending "/recipe?ingredients= Pasta Tomato ..." to the current url.
         <br>Click <a href="/recipe?ingredients= pasta tomato onion">here</a> for an example when using the ingredients: pasta, tomato and onion.
     </body></html>
     """
    return HELLO_HTML

@app.route('/recipe', methods=["GET"])
def recommend_recipe():
    ingredients = request.args.get('ingredients')

    return jsonify({"Ingredients":ingredients})
    # recipes = getRecipeRecommendations(5, [ingredients])
    # print(recipes)
    # response = {}
    # for index, row in recipes.iterrows():
    #     response[index] = {
    #                         'recipe': str(row['recipe_name']),
    #                         'score': str(row['scores']),
    #                         'ingredients': str(row['ingredients']),
    #                         'url': str(row['recipe_urls'])
    #                       }        
    # return jsonify(response)

if __name__ == "__main__":
   app.run(host="0.0.0.0", debug=False)