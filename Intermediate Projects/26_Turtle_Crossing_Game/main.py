import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Setup Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing")
screen.bgcolor("white")
screen.listen()

# Create Player, car, ScoreBoard
player = Player()
car = CarManager()
scoreboard = Scoreboard()

# Listen to Keyboard movement and move the turtle
screen.listen()
screen.onkeypress(player.up, "Up")
screen.onkeypress(player.down, "Down")

# Start the game
game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()  # Create new cars
    car.move_cars()  # move each cars

    # Detect collision with cars
    for a_car in car.all_cars:
        if a_car.distance(player) < 20:
            game_on = False  # End game
            scoreboard.game_over()  # Print Game Over

    # Detect if a player has reached the other side
    if player.ycor() > 270:
        player.go_to_start()  # Go to the beginning
        car.speed_up()  # Speed up the cars
        scoreboard.level_up()  # Update the Level
        scoreboard.write_level()  # Write the Score

screen.exitonclick()
