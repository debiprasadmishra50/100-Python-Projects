# import colorgram
#
# """Get colors in rgb from the image and store those in a list"""
# colors = colorgram.extract('hirst.jpg', 30)
# rgb = []
# for item in colors:
#     rgb.append((item.rgb[0], item.rgb[1], item.rgb[2]))

from turtle import Turtle, Screen
import turtle as t
import random
t.colormode(255)

color_list = [(200, 167, 110), (237, 241, 246), (144, 74, 52), (169, 152, 45), (58, 92, 119), (224, 203, 131), (136, 162, 180), (131, 34, 26), (51, 117, 89), (199, 94, 72), (143, 25, 30), (18, 97, 74), (69, 47, 40), (173, 146, 153), (150, 177, 152), (131, 70, 74), (56, 43, 46), (237, 174, 163), (184, 88, 94), (38, 58, 71), (28, 82, 89), (182, 204, 178), (242, 156, 160), (93, 144, 124), (20, 66, 57), (36, 65, 96), (108, 125, 154), (237, 241, 246), (144, 74, 52), (169, 152, 45)]
position = list(range(200, -300, -50))
tim = Turtle()
tim.speed(0)
tim.hideturtle()


def print_hirst():
    for row in range(10):
        tim.penup()
        tim.setx(-200)
        tim.sety(-1 * position[row])
        tim.pendown()
        for val in range(10):
            tim.dot(20, random.choice(color_list))
            tim.penup()
            tim.forward(50)


print_hirst()




screen = Screen()
screen.exitonclick()