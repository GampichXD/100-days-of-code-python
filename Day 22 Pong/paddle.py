# Step 3 : Create another paddle
from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.sch_wid = 5
        self.sch_len = 1
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=self.sch_wid, stretch_len=self.sch_len)
        self.penup()
        self.goto(x = x_pos, y = y_pos)
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

