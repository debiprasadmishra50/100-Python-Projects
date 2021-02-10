from turtle import Turtle
CHANGE_Y = 20


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def up(self):
        if self.ycor() < 240:
            new_y = self.ycor() + CHANGE_Y
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() > -240:
            new_y = self.ycor() - CHANGE_Y
            self.goto(self.xcor(), new_y)

