import pandas as pd
import re

def load_and_inspect_data():
    # Load the datasets
    recipes = pd.read_csv('recipes.csv')
    reviews = pd.read_csv('reviews.csv')

    # Display the first few rows of each dataframe to understand their structure
    print("Recipes Data:")
    print(recipes.head())

    print("\nReviews Data:")
    print(reviews.head())

    # Optionally, display the columns and their data types
    print("\nRecipes Columns and Data Types:")
    print(recipes.dtypes)

    print("\nReviews Columns and Data Types:")
    print(reviews.dtypes)
    
    return recipes, reviews

def parse_r_vector(r_vector_str):
    """Parse R-style c() vectors into Python lists."""
    if isinstance(r_vector_str, str) and r_vector_str.startswith('c('):
        # Remove the leading 'c(' and trailing ')'
        r_vector_str = r_vector_str[2:-1]
        # Split the string by commas
        items = r_vector_str.split(',')
        # Remove leading and trailing spaces and quotes, then convert to lower case
        items = [item.strip().strip('"').strip("'").lower() for item in items]
        return items
    return r_vector_str

def preprocess_data(recipes, reviews):
    # Apply the custom parser to RecipeIngredientParts and RecipeInstructions
    recipes['RecipeIngredientParts'] = recipes['RecipeIngredientParts'].apply(parse_r_vector)
    recipes['RecipeInstructions'] = recipes['RecipeInstructions'].apply(parse_r_vector)
    
    return recipes, reviews

def save_cleaned_data(recipes, file_path='cleaned_data.csv'):
    recipes.to_csv(file_path, index=False)
    print(f"Cleaned data saved to {file_path}")

if __name__ == "__main__":
    recipes, reviews = load_and_inspect_data()
    recipes, reviews = preprocess_data(recipes, reviews)
    print("\nProcessed Recipes Data:")
    print(recipes.head())
    save_cleaned_data(recipes)
