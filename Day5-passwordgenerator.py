#Password Generator Project
#while loops 

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
index = (letters+numbers+symbols)

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
def eazy():
  let=nr_letters
  sym=nr_symbols
  num=nr_numbers 
  password=''
  while let > 0:
    password += random.choice(letters)
    let -= 1
  while sym > 0:
    password += random.choice(symbols)
    sym -= 1
  while num > 0:
    password += random.choice(numbers)
    num -= 1
  print(password)
#eazy()

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

def hard():
  password=''
  let=nr_letters
  sym=nr_symbols
  num=nr_numbers 
  characters = let + sym + num
  while characters > len(password):
    choice = random.randrange(0,3)
    if choice == 0 and let > 0:
      password += random.choice(letters)
      let -= 1
    elif choice == 1 and sym > 0:
      password += random.choice(symbols)
      sym -= 1
    elif choice == 2 and num > 0:
      password += random.choice(numbers)
      num -= 1
  print(password)
hard()

  
    
