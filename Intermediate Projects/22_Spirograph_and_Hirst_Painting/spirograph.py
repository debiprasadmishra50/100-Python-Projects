from turtle import Turtle, Screen
import random, turtle as t

size = int(input("Enter the gap size in degrees(10-30 for better view): "))

t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    new_color = (r, g, b)
    return new_color


tim = Turtle()
tim.speed(speed=0)


def draw_spirograph(size_of_gap):
    for _ in range(360 // size_of_gap):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(size)


screen = Screen()
screen.exitonclick()
