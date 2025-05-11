from flask import Flask
import random

random_number = random.randint(0, 9)
print(random_number)

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width=300>'

@app.route('/<int:guess>')
def guess_number(guess):
    if guess > random_number:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExeHlvZnBzaWE5bmM4ZWhhaHV6cXJ6Z3VibXgwcGtjczFmM2R5azE4ZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/hrSMjnL0T6sVLSpoqo/giphy.gif'/>"
    elif guess < random_number:
        return "<h1 style='color: red'>Too low, try again!</h1>"\
               "<img src='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExc3J5d2JrNTY5YjllbGRlOWx1YWZpcGcyMXc5bmZ2eXVoM2I1Nmk1NSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/dBNnorhWYpoxG/giphy.gif'/>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHpwZDJud3NndGZqcnl3NmhhaDM2c3ZhZDZmcXcwYmcxd3Y2bDhkcCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ONuQzM11fjvoY/giphy.gif'/>"
    
if __name__ == "__main__":
    app.run(port=5050,debug=True)