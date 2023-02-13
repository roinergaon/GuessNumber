from flask import Flask, request, render_template
import random
import sys

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('number_guesser.html', min_range=min_range, max_range=max_range)

# Welcome message for the user
@app.route('/')
def welcome():
    return f"Welcome to the number guessing game!\nGuess a number between {min_range} and {max_range}."

# Check if the number of arguments passed through sys.args is correct
if len(sys.argv) != 4:
    print("Wrong input - try again")
    sys.exit()

# Retrieve the minimum and maximum range from the command line arguments
port = int(sys.argv[1])
min_range = int(sys.argv[2])
max_range = int(sys.argv[3])

# Generate a random number in the specified range
secret = random.randint(min_range, max_range)

# Get the user's guess and compare it to the secret number
@app.route('/guess', methods=['POST'])
def guess():
    guess = int(request.form['guess'])
    if guess > secret:
        return "Too big"
    elif guess < secret:
        return "Too small"
    else:
        return "Well done"

# Start the Flask server
if __name__ == '__main__':
    app.run(port=port, debug=True)
