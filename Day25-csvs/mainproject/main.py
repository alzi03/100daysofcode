import datasetup, turtlesetup

def stateguesser():
    state = datasetup.State()
    map = turtlesetup.Map()

    map.screensetup()

    title = 'State Checker'

    while not state.all():  # if all states have been guessed
        guess = map.userinput(correct=title)
        if state.checker(state=guess):
            map.initials(state=guess, coordinates=(state.coordinates(state=guess)))  # adds states
            title = 'Correct'
        else:
            title = 'Incorrect'
    print('Great Job! You got them all')
    map.byebye()



stateguesser()



