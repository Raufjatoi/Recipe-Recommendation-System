import speech_recognition as sr

def listen_for_ingredients():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please list your ingredients:")
        audio = r.listen(source)
    try:
        ingredients = r.recognize_google(audio)
        return ingredients
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")

user_ingredients = listen_for_ingredients()
if user_ingredients:
    recommendations = recommend_recipes(user_ingredients)
    print(recommendations[['title', 'ingredients']])
