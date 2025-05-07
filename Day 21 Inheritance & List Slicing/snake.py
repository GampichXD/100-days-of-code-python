from turtle import Turtle, Screen

STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
CURRENT_POSITION = []


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.tail = self.segments[len(self.segments) - 1]
    def create_snake(self):
        for position in STARTING_POSITION:
            # new_segment = Turtle(shape="square")
            # new_segment.color("white")
            # new_segment.penup()
            # new_segment.goto(position)
            # self.segments.append(new_segment)
            self.add_segment(position)
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
    # def eat(self):
    #     x_tail = self.tail.xcor()
    #     y_tail = self.tail.ycor()
    #     if self.head.heading() == RIGHT:
    #         x_new_tail = x_tail - 20
    #         y_new_tail = y_tail
    #     elif self.head.heading() == LEFT:
    #         x_new_tail = x_tail + 20
    #         y_new_tail = y_tail
    #     elif self.head.heading() == UP:
    #         x_new_tail = x_tail
    #         y_new_tail = y_tail - 20
    #     else:
    #         x_new_tail = x_tail
    #         y_new_tail = y_tail + 20
    #     new_tail_pos = (x_new_tail, y_new_tail)
    #     # new_segment = Turtle(shape="square")
    #     # new_segment.color("white")
    #     # new_segment.penup()
    #     # new_segment.goto(new_tail_pos)
    #     # self.segments.append(new_segment)
    #     self.add_segment(new_tail_pos)
    #Angle Yu' solution
    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
    def extend(self):
        self.add_segment(self.segments[-1].position())









