# import turtle
# import turtle as t ##aliasing
import turtle as t

# from turtle import * ## --> * is import everything, we can straight forward to use method without class
import random
# tim = turtle.Turtle()
tim = t.Turtle()


# tim = Turtle()
tim.shape("turtle")
tim.color("red")

# tom = Turtle()
# terry = Turtle()
# Challenge 1 : Make Square
# for i in range(4):
#     tim.forward(100) #pace
#     tim.right(90) #degree


# tim.forward(100) #pace
# tim.right(90) #degree
# tim.forward(100) #pace
# tim.right(90) #degree
# tim.forward(100) #pace
# tim.right(90) #degree

# Challenge 2 : Draw Dashed Line
# for i in range(15): # --> change the color
#     tim.color("red")
#     tim.forward(10)
#     tim.color("white")
#     tim.forward(10)
# Angela Yu's solution # --> write and unwrite pen
# for i in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

#Challenge 3 : Pentagon & More Draw Shape
# tim.right(36)
# tim.forward(100)
# for i in range(4):
#     tim.right(72)
#     tim.forward(100)
#Angela Yu's Solution
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(180)
#         tim.right(angle)
#
colors = ["black","midnight blue","light sea green","sea green","gold","maroon","indian red","indigo"]
#
# for i in range(3,11):
#     tim.color(random.choice(colors))
#     draw_shape(i)

#Challenge 4 : Random Walk

# t.colormode(255)
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color_tuple = (r, g, b)
#     return color_tuple
#
#
# direction = [0,90,180,270]
# tim.pensize(10)
# tim.speed("fastest")
# for i in range(200):
#     tim.color(random_color())
#     tim.setheading(random.choice(direction))
#     tim.forward(50)

#Challenge 5 : Spirograph
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple

tim.speed("fastest")
rounded = 360
amount_of_circle = 100
many_direction = rounded / amount_of_circle
angle_direction = tim.heading() #before, I use 0


for i in range(amount_of_circle):
    tim.color(random_color())
    tim.setheading(angle_direction)
    tim.circle(200)
    angle_direction += many_direction


screen = t.Screen()
screen.exitonclick()

# import heroes
# print(heroes.gen())



