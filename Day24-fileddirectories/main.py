# I work with files

# I really don't know what I was trying to say in the letter below, I thought of the most random thing possible

def message(name):
    with open(f'letter_to_{name}', mode='w') as file:
        file.write('''
Dear {name},

I hope this letter finds you in good health. I am writing to inquire about the number of spongebob
balloons that you currently have in stock. I am urgently trying to create the world's largest spongebob,
and I know that you for some reason one of the go to people for spongebob balloons. Please e-mail me back whenever possible,
as this is a matter of utmost urgency.

Best regards,
Alam''')

names = ['Red Ranger', 'Green Ranger', 'Yellow Ranger', 'Blue Ranger', 'Black Ranger', 'White Ranger', 'Pink Ranger', 'Gold Ranger']

for name in names:
    message(name)