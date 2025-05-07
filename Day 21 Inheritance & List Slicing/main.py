
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


food = Food()
snake = Snake()


screen.listen()
screen.onkey(fun=snake.up,key="Up")
screen.onkey(fun=snake.down,key="Down")
screen.onkey(fun=snake.right,key="Right")
screen.onkey(fun=snake.left,key="Left")
# Step 5 : Create a scoreboard
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Step 4 : Detect Collision with Food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.point()



# Step 6 : Detect Collisions with the Wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        game_is_on = False

# Step 7 : Detect Collisions with the Tail
    for segment in snake.segments[1:]:
        # if segment == snake.head:
        #     pass
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            game_is_on = False

# Slicing Array

# #Class Inheritance
# class Animal:
#     def __init__(self):
#         self.num_eyes = 2
#     def breathe(self):
#         print("Inhale, exhale")
#
# class Fish(Animal):
#     def __init__(self):
#         super().__init__()
#     def breathe(self):
#         super().breathe()
#         print("doing this underwater")
#     def swim(self):
#         print("moving in the water")
#
# nemo = Fish()
# nemo.swim()
# nemo.breathe()
# print(nemo.num_eyes)




screen.exitonclick()
