from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
from separator import Separator
import time

POSITION = [(-380, 0), (370, 0)]

# Set the Screen
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0)

# Create Paddles, Ball, ScoreBoard
l_paddle = Paddle(POSITION[0])  # Left Paddle
r_paddle = Paddle(POSITION[1])  # Right Paddle
for _ in range(12):
    separator = Separator()
ball = Ball()
scoreboard = ScoreBoard()

# Listen to Keyboard Input and control paddle movement
screen.listen()
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")


# Start the game
game_on = True
while game_on:
    time.sleep(ball.ball_speed)  # screen update
    screen.update()
    ball.move()  # Move the ball

    # Detect collision with up & down wall and bounce it
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    # Detect when collision with the paddle and bounce off
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -350:
        ball.bounce_x()

    # Detect when r_paddle misses
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_position()

    # Detect when l_paddle misses
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_position()








screen.exitonclick()

