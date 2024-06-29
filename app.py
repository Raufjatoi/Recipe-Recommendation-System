from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    user_ingredients = request.form['ingredients']
    recommendations = recommend_recipes(user_ingredients)
    return jsonify(recommendations[['title', 'ingredients']].to_dict('records'))

if __name__ == '__main__':
    app.run(debug=True)
