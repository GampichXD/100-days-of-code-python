from flask import Flask
# import random
app = Flask(__name__)
# print(random.__name__)
print(__name__) # __main__
# __name__ -> special attribute that tells you the name of the module
# __main__ -> name of the module that is being run

@app.route('/')
# Python decorator -> a special type of function that modifies another function
# first-class function, can be passed around as an argument to other functions, returned from other functions, and assigned to variables
# Nested function -> a function defined inside another function
# Functions can be returned from other functions

## Python decorators
# def decorator_function(original_function):
#     def wrapper_function():
#         print('Wrapper executed this before {}'.format(original_function.__name__))
#     return original_function()

def hello_world():
    return 'Hello, World!'

@app.route('/bye')
def say_bye():
    return 'Bye!'

if __name__ == '__main__':
    app.run(port=5050)

#Coding Exercise
import time
current_time = time.time()
print(current_time) # seconds since Jan 1st, 1970 

# Write your code below 👇

def speed_calc_decorator(function):
    def wrapper():
      start_time = time.time()
      function()
      end_time = time.time()
      run_time = end_time - start_time
      print(f"{function.__name__} run speed: {run_time}s")
    return wrapper
    
@speed_calc_decorator
def fast_function():
  for i in range(1000000):
    i * i
        
@speed_calc_decorator
def slow_function():
  for i in range(10000000):
    i * i

fast_function()
slow_function()

