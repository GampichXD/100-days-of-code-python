import colorgram
import turtle as t
import random

#Extract 6 colors from an image
# colors = colorgram.extract('image.jpg', 240)
# print(colors)
# first_color = colors[0]
# print(first_color)
# rgb = first_color.rgb
# print(rgb)
# hsl = first_color.hsl
# print(hsl)
# proportion = first_color.proportion
# print(proportion)
# red = rgb[0]
# print(red)
# # red = rgb.r
# print(red)
# saturation = hsl[1]
# print(saturation)
# saturation = hsl.s
# print(saturation)

# list_color = []
# for i in range(len(colors)):
#     color = colors[i]
#     red = color.rgb[0]
#     green = color.rgb[1]
#     blue = color.rgb[2]
#     tup_color = (red, green, blue)
#     list_color.append(tup_color)
#
# print(list_color)

list_col = [(133, 164, 202), (225, 150, 101), (30, 43, 64), (201, 136, 148), (163, 59, 49), (236, 212, 88), (44, 101, 147), (136, 181, 161), (148, 64, 72), (51, 41, 45), (161, 32, 29), (60, 115, 99), (59, 48, 45), (170, 29, 32), (215, 83, 73), (236, 167, 157), (230, 163, 168), (36, 61, 55), (15, 96, 71), (33, 60, 106), (172, 188, 219), (194, 99, 108), (106, 126, 158), (18, 83, 105), (175, 200, 188), (35, 150, 209), (65, 66, 56), (103, 140, 129), (164, 200, 214), (130, 129, 122)]
tim = t.Turtle()
tim.speed("fastest")
t.colormode(255)
x = -300
y = -300
tim.penup()
tim.hideturtle()
tim.setposition(x,y)
for i in range(10):
    tim.setposition(x,y)
    for j in range(10):
        # tim.pendown()
        tim.dot(20,random.choice(list_col))
        # tim.penup()
        tim.forward(50)
    y += 50

# Angela Yu's solution
# tim.speed("fastest")
# tim.penup()
# tim.hideturtle()
#
# tim.setheading(225)
# tim.forward(300)
# tim.setheading(0)
# number_of_dots = 100
#
# for dot_count in range(1, number_of_dots + 1):
#     tim.dot(20, random.choice(color_list))
#     tim.forward(50)
#
#     if dot_count % 10 == 0:
#         tim.setheading(90)
#         tim.forward(50)
#         tim.setheading(180)
#         tim.forward(500)
#         tim.setheading(0)



screen = t.Screen()
screen.exitonclick()








