from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = MOVE_INCREMENT

    def create_car(self):
        # make_a_car = True
        # while make_a_car:
        new_car = Turtle()
        new_car.shape("square")
        new_car.shapesize(stretch_wid=1,stretch_len=2)
        car_color = random.choice(COLORS)
        new_car.penup()
        new_car.setheading(180)
        new_car.color(car_color)
        y_axis = random.randint(-250,250)
        new_car.goto(x=300,y=y_axis)
        self.all_cars.append(new_car)


    def move_car(self):
        for car in self.all_cars:
            # time.sleep(0.1)
            # new_x_axis = car.xcor() + self.car_speed
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

