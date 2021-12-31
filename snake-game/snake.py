from turtle import Turtle

STEP = 20
EAST = 0
NORTH = 90
WEST = 180
SOUTH = 270


class Snake:
    def __init__(self):
        self.squares = []
        self.square()
        self.head = self.squares[0]

    def square(self):
        for index in range(3):
            new_square = Turtle(shape='square')
            new_square.color('white')
            new_square.penup()
            new_square.speed('slowest')
            new_square.setposition(y=0, x=0 - STEP * index)
            self.squares.append(new_square)

    def extend(self):
        new_square = Turtle(shape='square')
        new_square.color('white')
        new_square.penup()
        new_square.speed('slowest')
        new_square.setposition(self.squares[-1].position())
        self.squares.append(new_square)

    def move(self):
        for num in range(len(self.squares) - 1, 0, -1):
            position = self.squares[num - 1].position()
            self.squares[num].goto(position)
        self.head.forward(STEP)

    def right(self):
        if self.head.heading() != WEST:
            self.head.setheading(EAST)

    def up(self):
        if self.head.heading() != SOUTH:
            self.head.setheading(NORTH)

    def left(self):
        if self.head.heading() != EAST:
            self.head.setheading(WEST)

    def down(self):
        if self.head.heading() != NORTH:
            self.head.setheading(SOUTH)