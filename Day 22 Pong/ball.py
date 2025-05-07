# Step 4 : Create the ball and make it move
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.home()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        # self.speed("slowest")
        # self.setheading(37.1)
        # self.forward(470)
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)


# Step 5 : Detect collision with wall and bounce
    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def restart(self):
        self.home()
        self.move_speed = 0.1
        # self.x_move = 10
        # self.y_move = 10
        self.x_move *= -1


























