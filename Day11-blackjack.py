import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

# Draw a new card, let's user pick the value of the ace
def newcard():
  pick = random.choice(cards)
  if pick == 11:
    y = input('You drew an ace! Would you like for it to be equal to 1 or 11?:')
    if y == '1':
      pick = 1
    elif y == '11':
      pick = 11
  return pick

  
# Assiging risk level for computer to continue drawing or stop
compchoices = {
  2: [newcard],
  3: [newcard],
  5: [newcard],
  6: [newcard],
  7: [newcard],
  8: [newcard],
  9: [newcard],
  10: [newcard],
  11: [newcard],
  12: [newcard],
  13: [newcard],
  14: [newcard,newcard,newcard,'break'],
  15: [newcard,newcard,'break'],
  16: [newcard,'break','break'],
  17: [newcard,'break','break','break'],
  18: [newcard,'break','break','break','break'],
  19: [newcard,'break','break','break','break','break'],
  20: ['break'],
  21: ['break']  
}

def blackjack():
  '''Play a game of blackjack against a computer'''
  print('Welcome to Blackjack!\nTo win, you must get as close to 21 as possible while drawing cards without going over. If you go over, you lose. If the computer picks a closer number to 21 than you, you lose. Good luck!\n')
# Assigning initial values
  usersum = newcard() + newcard()
  c1 = random.choice(cards)
  c2 = random.choice(cards)
  if c2 == 11:
    if (compsum + 11) > 21:
      c2 = 1
  compsum = c1+c2
### User's picks
  while usersum <= 21:
    print(f'Your Total is: {usersum}')
    if usersum == 21:
      break
    again = input('Would you like to draw another card? y/n: ') 
    if again == 'y':
      usersum += newcard()
    elif again == 'n':
      break
    else:
      return(print('Invalid Choice'))
### Computer's picks
  while compsum <=21:
    action = random.choice(compchoices[compsum])
    if action == newcard:
      value = newcard()
      if value == 11:
        if (compsum + 11) > 21:
          value = 1
      compsum += value
    else:
      break
    if compsum > 21:
      break
### Various outcomes
  if usersum > 21:
    return(print(f'Your total is {usersum}, you lose!\nComputer\'s total Was {compsum}.'))
  print(f'Computer\'s total is: {compsum}')
  if compsum > 21:
    return(print(f'Computer\'s total is {compsum}, you win!'))
  if usersum>compsum:
    return(print('You Win!'))
  elif usersum == compsum:
    return(print('Draw'))
  else:
    return(print('You Lose!'))

blackjack()



