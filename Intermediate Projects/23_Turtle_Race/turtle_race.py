from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=600, height=500)
colors = ["red", "orange", "blue", "purple", "green", "yellow"]
user_bet = screen.textinput(title="Make your bet", prompt=f"Which turtle will win the race? Enter a Color {colors}: ")
y = -180
all_turtles = []


def create_turtles(y_coordinate):
    for item in range(6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.penup()
        new_turtle.color(colors[item])
        y_coordinate += 50
        new_turtle.goto(x=-270, y=y_coordinate)
        all_turtles.append(new_turtle)


create_turtles(y)


race_on = False
if user_bet:
    race_on = True
else:
    print("Please place a bet on which turtle will win the race")


def game_on(is_race_on):
    while is_race_on:
        for turtle in all_turtles:
            if turtle.xcor() > 260:
                is_race_on = False
                winning_turtle = turtle.pencolor()
                if winning_turtle == user_bet:
                    print(f"You Won!! The {winning_turtle} turtle won the race.")
                else:
                    print(f"You Lost!! The {winning_turtle} turtle won the race.")

            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)


game_on(race_on)





screen.exitonclick()
