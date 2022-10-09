
import random
hangmanpics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
word_list = ["aardvark", "baboon", "animal", "monkey", "train", "car" ,"zoo", "auditorium", "theater", "recital", "recitation", "laptop", "computer", "phone", "port", "company", "sweater", "jacket"]



def hangman(): 
  choice=random.choice(word_list)
  display = '_' * len(choice)
  wrong =  0 
  guesses=[] #puts the guesses so player can't be penalized for repeats
  while wrong < 7: #timer for num of gueses
    guess=input('Guess a letter: ').lower()
    index = 0
    indexes=[]
    if guess in choice:
      guesses.append(guess)
      for letter in choice:
        if letter == guess:
          indexes.append(index)
        index+=1
      for value in indexes:
        display = display[:value] + guess + display[value+1:] #rewriting output to include correct guesses
    else:
      print(hangmanpics[wrong]) #poor hangman
      guesses.append(guess)
      wrong += 1
    print('\n')
    print(display)
    if '_' in display:
      continue
    else:
      print('Good Job!') #winning
      break
  if wrong == 7 : 
    print (f'Better luck next time, your word was {choice}')
    
  
hangman()
       
    
  
