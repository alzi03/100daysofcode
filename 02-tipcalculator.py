#tip calculator
#data types + f strings

#Write your code below this line 👇
bill = float(input("What is your total? "))
num = int(input("Number of people: "))
tip = 1 + float(input("Percent Tip: ").rstrip("%"))/100


perperson = "{:.2f}".format(((bill/num)*tip))
perperson
  
print(f'Each person should pay ${perperson}')
