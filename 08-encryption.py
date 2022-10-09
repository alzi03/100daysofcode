#learning about function inputs

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(d, t, s):
  if d == ('decode'):
    s = s * -1
  newstr=''
  for letter in t:
    index = alphabet.index(letter) #finding index of each letter
    newletter = alphabet[index+s] #adding new letter to str
    newstr += newletter  
  print(f'The encoded text is {newstr}.')
  
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
encrypt(d=direction, t=text, s=shift) 


