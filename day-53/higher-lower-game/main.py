from flask import  Flask
import random
random_number = random.randint(0,9)
print(random_number)
app = Flask(__name__)

@app.route('/')
def home():
    return ('<h1>Guess a number between 0 and 9</h1>'
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">')
@app.route('/<int:guess>')
def guess_number(guess):
    if guess > random_number:
        return ('<h1>The number is too high</h1>'
                '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">')
    elif guess < random_number:
        return ('<h1>The number is too low</h1>'
                '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">')
    elif guess == random_number:
        return ('<h1>The number is correct</h1>'
                '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">')
    else:
        return '<h1>Enter valid guess</h1>'
if __name__ == "__main__":
    app.run(debug=True)