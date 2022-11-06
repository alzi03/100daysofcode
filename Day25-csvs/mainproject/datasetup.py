import pandas

class State:

    def __init__(self):
        self.correct=[]
        self.data = pandas.read_csv('references/states.csv')
        self.stateList = self.data.State.to_list()

    def checker(self, state):
        if state in self.stateList:  # check's to see if the input is a correct state
            if state not in self.correct:
                self.correct.append(state)  # to ensure no repeats
                return True
        return False

    def abbreviation(self, state):  # determines what the turtle will write
        state = self.data[self.data.State == state]
        initial = state.Abbreviation.to_list()[0]
        return initial

    def coordinates(self, state):  # determines where the state is
        state = self.data[self.data.State == state]
        x = state.Position.to_list()
        return x[0]

    def all(self):  # checks to see if all states have been guessed
        if len(self.correct) == 50:
            return True
        return False





