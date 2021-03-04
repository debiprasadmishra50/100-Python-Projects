from turtle import Turtle


class Separator(Turtle):
    y = -270

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(1.5, 0.2)
        self.goto(x=0, y=Separator.y)
        Separator.y += 50
