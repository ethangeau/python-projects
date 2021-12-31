from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.speed('fastest')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color('red')
        self.update()

    def update(self):
        x = randint(-360, 360)
        y = randint(-360, 360)
        self.goto(x, y)

