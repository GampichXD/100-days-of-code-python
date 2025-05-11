# https://www.mysite.com/Angela

from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper_function():
        return f'<b>{function()}</b>'
    return wrapper_function

def make_emphasis(function):
    def wrapper_function():
        return f'<em>{function()}</em>'
    return wrapper_function

def make_underlined(function):
    def wrapper_function():
        return f'<u>{function()}</u>'
    return wrapper_function

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
    '<p>This is a paragraph</p>' \
    '<img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExemViYTRtbHptaHQwN2N3cDE2cTdkNWUydDFxNzQ4ZGVmejJtc2pkOCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ONuQzM11fjvoY/giphy.gif" width=300>' \

@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return 'Bye!'

@app.route('/username/<name>/<int:number>') # variable section of the URL
# if you erase /username/ from the URL before you re-run, it will not work
# <converter:variable_name> -> converter is the type of variable you want to pass
def greet(name, number):
    return f'Hello there, {name}, you are {number} years old!'

if __name__ == '__main__':
    app.run(port=5050, debug=True)
# debug=True -> automatically reloads the server when you make changes to the code