import turtle


class Map:
    def __init__(self):
        self.tim = turtle.Turtle()  # Tim
        self.tim.penup()
        self.screen = turtle.Screen()

    def screensetup(self):
        self.screen.bgpic('references/USMAP.gif')  # setting background

    def initials(self, state, coordinates):  # turtle adds state letters if the user gets a correct answer
        coords = coordinates.split(',')
        self.tim.goto(x=int(coords[0]), y=int(coords[1]))
        self.tim.write(arg=f'{state}',align='Center', font=('Arial', 10, 'normal'))

    def userinput(self, correct):  # reformats the user input to ensure it is in line with data
        guess = self.screen.textinput(title=f'{correct}', prompt='Enter A State')
        guess = ' '.join(word[0].upper() + word[1:] for word in guess.split())
        return guess

    def byebye(self):  # lets the user decide when to leave
        self.screen.exitonclick()





