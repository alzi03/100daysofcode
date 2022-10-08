#scope of functions and variables

import random

#set difficulty using dictionary

difficulty = {
  'easy':10,
  'hard':5
}

#various outcomes with guesses
def guesscheck(g,n,m):
  if g == n:
    return(print(f'You got it! The answer is {g}'))
  else:
    m -= 1
    if g > n:
      print('Too High')
    else:
      print('Too Low')
    return(print(f'You have {m} guesses left'))
    
      

def play():
  #choose difficult
  mode = difficulty[input('Welcome to the Number Guessing Game!\nI\'m thinking of a number between 1 and 100.\nChoose a difficulty (easy/hard): ').lower()]
  num = random.randrange(1,101)
  print(num)
  guess = 0
  while guess != num: 
    guess = int(input('Take a guess: '))
    guesscheck(g=guess,n=num,m=mode) #checking to see if guess is right
    mode -= 1
    if mode == 0:
      break
play()
  
  
  
    
  

