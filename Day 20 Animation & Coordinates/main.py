#Nokia 3310 --> Snake Game

# Step 1 : Create body snake
from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
#1 turtle
# tim = Turtle(shape="square")
# tim.color("white")
# tim.shapesize(stretch_wid=1,stretch_len=3,outline=1)
# segments = []
# #
# # #3 turtles
# x_set = 0
# for square in range(3):
#     new_snake = Turtle(shape="square")
#     new_snake.color("white")
#     new_snake.penup()
#     new_snake.goto(x=x_set,y=0)
#     x_set -= 20
# # Step 2 : Move the snake
#     segments.append(new_snake)

snake = Snake()
# Step 3 : Control the Snake (Keypress)
screen.listen()
screen.onkey(fun=snake.up,key="Up")
screen.onkey(fun=snake.down,key="Down")
screen.onkey(fun=snake.right,key="Right")
screen.onkey(fun=snake.left,key="Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # for segm_num in range(len(segments) - 1, 0, -1):
    #     new_x = segments[segm_num - 1].xcor()
    #     new_y = segments[segm_num - 1].ycor()
    #     segments[segm_num].goto(new_x, new_y)
    # segments[0].forward(20)



screen.exitonclick()












