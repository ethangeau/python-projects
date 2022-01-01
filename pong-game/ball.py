from turtle import Turtle
from random import choice

ANGLE = [30, 60, 120, 150, 210, 240, 300, 330]


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.setheading(choice(ANGLE))

    def move(self):
        self.forward(20)

    def hit_wall(self):
        angle = self.heading() * -1
        self.setheading(angle)

    def hit_paddle(self):
        angle = 180 - self.heading()
        self.setheading(angle)

    def reset(self):
        self.goto(x=0, y=0)
        self.setheading(choice(ANGLE))