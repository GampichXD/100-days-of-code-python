import turtle
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

# def move_forward():
#     tim.forward(10)



# Functions as Inputs
# function_a(function_b)

#Higher Order Functions
# screen.listen()
# screen.onkey(key="w",fun=move_forward)

#Challenge : Etch-A-Sketch

def forwards():
    tim.forward(20)

def backwards():
    tim.backward(20)

def counter_clockwise():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def clockwise():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clear_drawing():
    tim.home()
    tim.clear()


screen.listen()
screen.onkey(key="w",fun=forwards)
screen.onkey(key="s",fun=backwards)
screen.onkey(key="a",fun=counter_clockwise)
screen.onkey(key="d",fun=clockwise)
screen.onkey(key="c",fun=clear_drawing)
screen.exitonclick()

#state --> other attribute or method of any object



