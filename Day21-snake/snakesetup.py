from turtle import Turtle, Screen
import time


class Snaking:

    def __init__(self):
        self.turtles = []  # list of every turtle in the snake
        self.make()

        self.front = self.turtles[0]  # defining front snake

        # scoreboard
        self.score = 0
        file = (open('highscore.txt', 'r'))
        self.highscore = int(file.read()[0])
        self.writer = Turtle()

    def window(self, screen):  # setting up the screen
        screen.setup(width=600, height=600)
        screen.title('Snake')
        screen.bgcolor('black')
        screen.tracer(0)
        screen.listen()

    def make(self):

        snake = Turtle()  # making a list with first three turtles and having them on the screen
        self.turtles.append(snake)
        x, y = snake.xcor(), snake.ycor()
        snake.penup()
        snake.color('blue'), snake.shape('square')
        for i in range(1, 3):  # creating new turtles
            self.turtles.append(snake.clone())
            self.turtles[i].goto(x - 20 * i, 0)

    def scoretracker(self, apples):  # making a turtle keep track of score
        self.writer.clear()
        self.writer.hideturtle()
        self.writer.setpos(0, 250)
        self.writer.pencolor('white')
        self.writer.write(arg=f'Score: {apples} High Score: {self.highscore}', move=False, align='center', font=("Comic Sans", 24, 'normal'))

    def addpoint(self):  # point system
        x = Turtle()
        x.penup(), x.color('blue'), x.shape('square')

        old = self.turtles[-1]
        self.turtles.append(x)

        followx = old.xcor()
        followy = old.ycor()

        if old.heading() == 0:  # set based on heading of last turtle
            x.setx(followx - 20)
            x.sety(followy)
        elif old.heading() == 90:
            x.setx(followx)
            x.sety(followy - 20)
        elif old.heading() == 180:
            x.setx(followx + 20)
            x.sety(followy)
        else:
            x.setx(followx)
            x.sety(followy + 20)

        self.score += 1  # scoreboard

    def highestscorer(self):
        file = open('highscore.txt', 'w')
        if self.score > self.highscore:
            file.write(str(self.score))
        self.score = 0
        self.scoretracker(apples=self.score)
        file.close()


    def death(self):  # death is inevitable
        if self.front.xcor() >= (300) or self.front.xcor() <= -300:
            self.highestscorer()
            return True
        if self.front.ycor() >= (300) or self.front.ycor() <= -300:
            self.highestscorer()
            return True
        for i in range(1, len(self.turtles)):
            if self.front.distance(self.turtles[i]) <= 10:
                self.highestscorer()
                return True

    def forward(self):  # each turtle always moving to the position of the turtle in front of it
        for i in range(len(self.turtles) - 1, 0, -1):
            x, y = self.turtles[i - 1].xcor(), self.turtles[i - 1].ycor()
            self.turtles[i].goto(x, y)
            self.turtles[i - 1].forward(20)

    # the various key presses
    def up(self):
        if self.front.heading() != 270:
            self.front.setheading(90)

    def left(self):
        if self.front.heading() != 0:
            self.front.setheading(180)

    def down(self):
        if self.front.heading() != 90:
            self.front.setheading(270)

    def right(self):
        if self.front.heading() != 180:
            self.front.setheading(0)
























