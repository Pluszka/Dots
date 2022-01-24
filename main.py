# from colorgram import extract
#
# colors = extract('damien-hirst-bromobenzotrifluoride.jpg', 30)
#
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
import turtle

nonwhite_colors = [
    (222, 163, 66), (19, 45, 87), (136, 61, 84), (177, 60, 44),
 (126, 40, 61), (21, 86, 61), (59, 48, 37), (250, 194, 42),
 (13, 117, 146), (57, 146, 72), (229, 86, 36), (231, 172, 190),
 (57, 71, 39), (197, 102, 134), (197, 125, 150), (156, 191, 185),
 (30, 67, 58), (166, 204, 202), (62, 26, 45),
 (145, 165, 181), (6, 79, 111), (35, 44, 99), (71, 153, 84),
 (120, 41, 33), (170, 203, 205), (223, 178, 169)
 ]


from turtle import Turtle, Screen
from random import choice

turtle.colormode(255)

Andy = Turtle()
Andy.hideturtle()
Andy.penup()
Andy.goto(-300, 250)
print(Andy.position())

#TODO 1 def place to start

def one_line():
    for spot in range(20):
        Andy.dot(13, choice(nonwhite_colors))
        Andy.forward(30)

for lines in range(20):
    one_line()
    Andy.setheading(270)
    Andy.forward(30)
    Andy.setheading(180)

screen = Screen()
screen.exitonclick()
