import pandas as pd

# Load the dataset
recipes = pd.read_csv('recipes.csv')  # Update the path to your dataset

# Display the first few rows to understand the structure
print(recipes.head())

# Fill missing values
recipes.fillna('', inplace=True)

# Normalize ingredients (e.g., stripping whitespace, converting to lowercase)
def normalize_ingredients(ingredients):
    return [ingredient.strip().lower() for ingredient in ingredients.split(',')]

recipes['normalized_ingredients'] = recipes['ingredients'].apply(normalize_ingredients)

# Display the preprocessed data
print(recipes[['title', 'normalized_ingredients']].head())

