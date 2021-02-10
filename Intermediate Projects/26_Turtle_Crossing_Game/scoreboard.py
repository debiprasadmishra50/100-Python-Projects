from turtle import Turtle

FONT = ("Algerian", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        self.level = 1
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(-280, 250)
        self.write_level()

    def level_up(self):
        self.level += 1

    def write_level(self):
        self.clear()
        self.write(f"Level: {self.level}", move=False, align="left", font=FONT)

    def game_over(self):
        self.goto(-80, 0)
        self.write("GAME OVER", font=FONT)
