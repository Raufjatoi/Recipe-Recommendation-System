import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class RecipeRecommender:
    def __init__(self, recipe_data_path):
        self.recipes = pd.read_csv(recipe_data_path)
        self.tfidf = TfidfVectorizer(stop_words='english', tokenizer=self.custom_tokenizer)
        self.tfidf_matrix = self.tfidf.fit_transform(self.recipes['RecipeIngredientParts'].astype(str))

    def custom_tokenizer(self, text):
        return text.strip('[]').replace("'", "").split(',')

    def recommend(self, ingredients):
        query = ' '.join(ingredients)
        query_tfidf = self.tfidf.transform([query])
        cosine_similarities = cosine_similarity(query_tfidf, self.tfidf_matrix)
        top_indices = cosine_similarities.argsort()[0][-5:][::-1]
        recommendations = self.recipes.iloc[top_indices]
        return recommendations

if __name__ == "__main__":
    recommender = RecipeRecommender('cleaned_data.csv')
    ingredients = ['chicken', 'rice', 'onion']
    recommendations = recommender.recommend(ingredients)
    print("\nRecommended Recipes:")
    # Update the column names to match those in your CSV file
    print(recommendations[['Name', 'RecipeIngredientParts']])
