from turtle import Turtle, Screen
import random
import colorgram as cg


class HisrtPainter:

    def __init__(self):
        self.color_database = None

    def color_extract(self, image_path):
        colors = cg.extract(image_path, 20)
        rgb_colors = []
        for color in colors:
            r = color.rgb.r
            g = color.rgb.g
            b = color.rgb.b
            rgb_color = r, g, b
            rgb_colors.append(rgb_color)
        self.color_database = rgb_colors

    def draw_paint(self):
        turtle = Turtle()
        turtle.speed('fastest')
        turtle.shape("arrow")
        turtle.penup()
        turtle.hideturtle()
        turtle.setheading(225)
        turtle.forward(350)
        screen = Screen()
        screen.colormode(255)

        for time in range(10):
            turtle.setheading(180 * time % 360)
            turtle.dot(20, random.choice(self.color_database))
            for _ in range(9):
                turtle.forward(50)
                turtle.dot(20, random.choice(self.color_database))
            turtle.setheading(90)
            turtle.forward(50)

        screen.exitonclick()


painter = HisrtPainter()
painter.color_extract('hisrt.jpg')
painter.draw_paint()
