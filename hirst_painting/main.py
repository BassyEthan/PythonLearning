from turtle import Turtle, Screen
import random


# import colorgram
# colors = colorgram.extract('image.jpg', 30)
#
# list = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     list.append(new_color)
#
# print(list)

pen = Turtle()

pen.penup()
pen.goto(-235, -235)  # Coordinates of the bottom-left corner
pen.pendown()
pen.screen.colormode(255)
color_list = [(240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
pen.pensize(20)
pen.speed("fastest")

current_y = -235

for y in range(10):
    pen.screen.colormode(255)
    for x in range(10):
        pen.color(random.choice(color_list))
        pen.forward(0)
        pen.penup()
        pen.forward(50)
        pen.pendown()
    current_y += 50
    pen.penup()
    pen.goto(-235, current_y)  # Coordinates of the bottom-left corner
    pen.pendown()












screen = Screen()
screen.exitonclick()
