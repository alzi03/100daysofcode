#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
bill = float(input("What is your total? "))
num = int(input("Number of people: "))
tip = 1 + float(input("Percent Tip: ").rstrip("%"))/100


perperson = "{:.2f}".format(((bill/num)*tip))
perperson
  
print(f'Each person should pay ${perperson}')
