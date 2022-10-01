#list indexing

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
outcomes = [['rockpaper', 'You Win!'], ['rockscissors', 'You Lose!'],
            ['rockrock', 'Draw!'], ['paperpaper', 'Draw!'],
            ['paperscissors', 'You Win!'], ['paperrock', 'You Lose!'],
            ['scissorsscissors', 'Draw!'], ['scissorsrock', 'You Win!'],
            ['scissorspaper', 'You Lose!']]


def rps():
    choice = input('Rock, Paper, Scissors\n').lower()
    ai = ['rock', 'paper', 'scissors'][random.randrange(0, 2)]
    outcome = ai + choice
    print(f'You chose...\n{choice}')
    if choice == 'rock':
        print(rock)
    elif choice == 'paper':
        print(paper)
    else:
        print(scissors)
    print(f'Computer chose...\n{ai}')
    if ai == 'rock':
        print(rock)
    elif ai == 'paper':
        print(paper)
    else:
        print(scissors)
    for item in outcomes:
        if outcome in item:
            a = print(item[1])  #checking list to find outcome
    if input('Play Again(y/n)? ').lower() == 'y':
        rps()


rps()
