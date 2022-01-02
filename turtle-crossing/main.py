import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()
screen.onkey(player.move, 'Up')

turn = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if turn % 6 == 0:
        car_manager.new_car()

    car_manager.move_cars()

    if player.is_reach_finish_line():
        player.reset()
        car_manager.level_up()
        scoreboard.level_up()

    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    turn += 1

screen.exitonclick()
