from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor('black')
screen.title('Pong Game')
screen.setup(width=800, height=600)
screen.tracer(0)

left_paddle = Paddle((-390, 0))
right_paddle = Paddle((380, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.up, 'Up')
screen.onkey(right_paddle.down, 'Down')
screen.onkey(left_paddle.up, 'w')
screen.onkey(left_paddle.down, 's')

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -270:
        ball.hit_wall()

    if (ball.distance(right_paddle) < 50 and ball.xcor() > 360) or\
            (ball.distance(left_paddle) < 50 and ball.xcor() < -360):
        ball.hit_paddle()

    if ball.xcor() > 380:
        ball.reset()
        scoreboard.left_point()

    if ball.xcor() < -380:
        ball.reset()
        scoreboard.right_point()

screen.exitonclick()
