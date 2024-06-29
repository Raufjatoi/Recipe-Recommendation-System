from flask import Flask, render_template, request
import pandas as pd
from recommender import RecipeRecommender

app = Flask(__name__)

# Initialize the recipe recommender
recommender = RecipeRecommender('cleaned_data.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    if request.method == 'POST':
        ingredients = request.form['ingredients']
        ingredients_list = [ingredient.strip() for ingredient in ingredients.split(',')]
        recommendations = recommender.recommend(ingredients_list)
        return render_template('recommendations.html', recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
