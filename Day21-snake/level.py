from turtle import Turtle
import random


class Dot(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid = 0.5, stretch_len=0.5)
        self.color('white')
        self.speed('fastest')

    def go(self):
        xcor, ycor = random.randrange(-285, 285), random.randrange(-285, 285)
        self.goto(xcor, ycor)

    def disappear(self):
        Dot.go(self)
