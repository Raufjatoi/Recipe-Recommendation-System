# Personalized Recipe Recommendation System

Welcome to the Personalized Recipe Recommendation System! This project suggests recipes based on ingredients you have at home, dietary preferences, and past cooking history. It also integrates a virtual kitchen assistant to make your cooking experience seamless and interactive.

## Features
- **Personalized Recipe Suggestions**: Get recipe recommendations based on the ingredients you have.
- **Dietary Preferences**: Filter recipes according to dietary restrictions or preferences.
- **Past Cooking History**: Enhance recommendations based on your previous cooking activities.
- **Virtual Kitchen Assistant**: Interact with a virtual assistant for cooking instructions, ingredient substitutions, and more.
- **Web Application**: User-friendly interface for easy interaction and recipe browsing.

## Dataset
We used the [Food.com Recipes and Reviews](https://www.kaggle.com/irkaal/foodcom-recipes-and-reviews) and [Recipes and Interactions](https://www.kaggle.com/shuyangli94/food-com-recipes-and-user-interactions) datasets from Kaggle for our recipe data.

## Installation

1. **Clone the repository**
    ```sh
    git clone https://github.com/yourusername/recipe-recommendation-system.git
    cd recipe-recommendation-system
    ```

2. **Create and activate a virtual environment**
    ```sh
    python3 -m venv env
    source env/bin/activate
    ```

3. **Install the required dependencies**
    ```sh
    pip install -r requirements.txt
    ```

4. **Download the datasets and place them in the `data` folder**

5. **Run the application**
    ```sh
    python app.py
    ```

## Usage

1. **Launch the Web Application**
    - Open your web browser and go to `http://127.0.0.1:5000`.

2. **Enter Your Ingredients**
    - In the input field, enter the ingredients you have at home, separated by commas.

3. **Get Recommendations**
    - Click the "Get Recommendations" button to view personalized recipe suggestions.

4. **Interact with the Virtual Kitchen Assistant**
    - Use the virtual assistant to get step-by-step cooking instructions, ingredient substitutions, and more.

## File Structure

