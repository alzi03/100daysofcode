#going through values in dictionaries


logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

def auction():
  print(logo)
  bids={}
  print('Welcome to the secret auction.')
  bids[input('What is your name?: ')] = (int(input('What\'s your bid?: '))) #adding keys/values
  morbid = 0
  max = 0 #highest bid
  while morbid == 0: #while loop to continue adding bids
    other = input('Are there other bidders? Type yes or no.\n')
    if other == 'yes':
      bids[input('What is your name?: ')] = (int(input('What\'s your bid?: ')))
      continue
    elif other == 'no':
      for bid in bids:
        if bids[bid] > max:
          name = bid 
          max = bids[bid] #could also use max(bids.values()), unsure how to get index to assign name value
      print(f'The winner is {name} with a bid of {max}.')
      morbid += 1
    else:
      print("Invalid")
      break
    
auction()
      
    
    
  
