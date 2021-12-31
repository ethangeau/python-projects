from turtle import Turtle, Screen
from snake import Snake
from food import Food
from score import Score
import time

snake = Snake()
food = Food()
scoreboard = Score()
screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

screen.listen()
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')

is_game_on = True
while is_game_on:
    snake.move()
    screen.update()
    time.sleep(0.2)

    if snake.head.distance(food) < 15:
        food.update()
        scoreboard.update()
        snake.extend()

    if snake.head.xcor() < -380 or snake.head.xcor() > 370 \
            or snake.head.ycor() < -370 or snake.head.ycor() > 380:
        is_game_on = False
        scoreboard.game_over()

    for square in snake.squares[1:]:
        if snake.head.distance(square) < 10:
            is_game_on = False
            scoreboard.game_over()

screen.exitonclick()
