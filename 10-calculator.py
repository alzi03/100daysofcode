#calculator using defined outputs
operands = ('+','-','*','/')

#defining operations
def add(a,b):
  '''Add'''
  return a + b
def subtract(a,b):
  '''Subtract'''
  return a - b
def multiply(a,b):
  '''Multiply'''
  return a * b
def divide(a,b):
  '''Divide'''
  return a / b


def calculator():
  one = float(input("Enter the first number: ")) 
  goagain = True
  while goagain != False:
    print('Choose your operand')
    for a in operands:
      print(a)
    operand = input("")
    two = float(input("Enter the second number: "))
    if operand == '+':
      soln = add(one,two)
      print(f'{one} {operand} {two} is equal to {soln}')
    elif operand == '-':
      soln = subtract(one,two)
      print(f'{one} {operand} {two} is equal to {soln}')
    elif operand == '*':
      soln = multiply(one,two)
      print(f'{one} {operand} {two} is equal to {soln}')
    elif operand == '/':
      soln = divide(one,two)
      print(f'{one} {operand} {two} is equal to {soln}')
    else:
      print ("Invalid paramaters, try again")  #if something isn't adhering to the paramaters
      return
    one=soln #continue with answer
    if (input('Go again with the answer as your starting number? y/n ')) == 'n':
      goagain = False
      calculator() #restarting from the beginning
    
calculator()

