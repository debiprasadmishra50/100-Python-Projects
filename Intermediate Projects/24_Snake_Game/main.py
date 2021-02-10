from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

# Create Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # Turn off the animation

# Create Snake, Food
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()  # Listen to the Keyboard Input
# Control the Snake Movement
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Move Snake
game_on = True
while game_on:
    screen.update()  # Update the screen for each movement
    time.sleep(0.1)
    # Move the Snake
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()  # Increase snake size after each food
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 280 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.snakes[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()











screen.exitonclick()