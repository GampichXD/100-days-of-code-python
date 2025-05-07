from turtle import Turtle, Screen



# import time
#
# screen = Screen()
# screen.setup(width=600, height=600)
# screen.bgcolor("black")
# screen.title("My Snake Game")
# screen.tracer(0)
# x_set = 0
STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    def create_snake(self):
        for position in STARTING_POSITION:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
    def move(self):
        for segm_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segm_num - 1].xcor()
            new_y = self.segments[segm_num - 1].ycor()
            self.segments[segm_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

# a = Snake()
#
# game_is_on = True
# while game_is_on:
#     screen.update()
#     time.sleep(0.1)
#     a.move()
#     a.up()
#
# screen.exitonclick()



