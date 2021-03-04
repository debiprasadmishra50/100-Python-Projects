from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def up(self):
        if self.ycor() < FINISH_LINE_Y:
            self.forward(MOVE_DISTANCE)

    def down(self):
        if self.ycor() > STARTING_POSITION[1]:
            self.forward(-1 * MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)
