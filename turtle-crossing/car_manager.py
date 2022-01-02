from turtle import Turtle
from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def new_car(self):
        new_car = Turtle()
        new_car.shape('square')
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(choice(COLORS))
        new_car.penup()
        new_car.setheading(180)
        new_car.goto(300, randint(-250, 250))
        self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.speed)

    def level_up(self):
        self.speed += MOVE_INCREMENT



