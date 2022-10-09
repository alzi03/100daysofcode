import random
from art import logo,vs
from game_data import data

def higherlower():
  '''Play a game of higher and lower'''
  print(logo)
  c1 = random.choice(data)
  data.remove(c1)
  c1name,c1descr,c1spot,c1followers = c1['name'],c1['description'],c1['country'],c1['follower_count']
  c2=random.choice(data)
  data.remove(c2)
  c2name,c2descr,c2spot,c2followers = c2['name'],c2['description'],c2['country'],c2['follower_count']
  score=0
  while 1==1:
    print(f'Compare {c1name}, a {c1descr} from {c1spot}')
    print(vs)
    print(f'Against {c2name}, a {c2descr} from {c2spot}') 
    choice = input('Which is higher? A or B:')
    if (choice == 'A' and c1followers > c2followers) or (choice=='B' and c2followers>c1followers):
      score+=1
      print(f'Correct! Your score is {score}.')
      c1name,c1descr,c1spot,c1followers = c2name,c2descr,c2spot,c2followers
      c2=random.choice(data)
      data.remove(c2)
      c2name,c2descr,c2spot,c2followers = c2['name'],c2['description'],c2['country'],c2['follower_count']
      continue
    else:
      print(f'Wrong Choice! Your score was {score}')
      break
  return
higherlower()
      
    
  
  
  
  