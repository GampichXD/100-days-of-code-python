from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color")
colors = ["red","orange","yellow","green","blue","purple"]
all_turtle = []

# tim = Turtle(shape="turtle")
# tom = Turtle(shape="turtle")
# tam = Turtle(shape="turtle")
# tum = Turtle(shape="turtle")
# tem = Turtle(shape="turtle")
# teem = Turtle(shape="turtle")
#
# name = [tim, tom, tam, tum, tem, teem]
y_set = 200
for turtle in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle])
    new_turtle.penup()
    y_set -= 50
    new_turtle.goto(x =-230,y=y_set)
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for a_turtle in all_turtle:
        if a_turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = a_turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You've won! The {winning_turtle} turtle is the winner")
            else:
                print(f"You've lost! The {winning_turtle} turtle is the winner")
        random_distance = random.randint(0, 10)
        a_turtle.forward(random_distance)

# tim.penup()

# tim.goto(x=-230, y=-100)
screen.exitonclick()