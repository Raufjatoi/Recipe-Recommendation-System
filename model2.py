from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Create a TF-IDF matrix of ingredients
tfidf = TfidfVectorizer(tokenizer=lambda x: x, lowercase=False)
tfidf_matrix = tfidf.fit_transform(recipes['normalized_ingredients'].apply(lambda x: ' '.join(x)))

# Function to recommend recipes
def recommend_recipes(user_ingredients, num_recommendations=5):
    user_ingredients = normalize_ingredients(user_ingredients)
    user_tfidf = tfidf.transform([' '.join(user_ingredients)])
    cosine_sim = cosine_similarity(user_tfidf, tfidf_matrix)
    recommendations = cosine_sim.argsort()[0, -num_recommendations:][::-1]
    return recipes.iloc[recommendations]

# Example usage
user_ingredients = 'tomato, cheese, basil'
recommendations = recommend_recipes(user_ingredients)
print(recommendations[['title', 'ingredients']])
