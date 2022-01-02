from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 290


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('red')
        self.hideturtle()
        self.penup()
        self.setposition(STARTING_POSITION)
        self.setheading(90)
        self.showturtle()

    def move(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def is_reach_finish_line(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        else:
            return False

    def reset(self):
        self.goto(STARTING_POSITION)

