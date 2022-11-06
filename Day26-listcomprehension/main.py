phonetic = {'A': 'Apple', 'B': 'Banana', 'C': 'Cat', 'D': 'Dog', 'E': 'Elephant', 'F': 'Fire', 'G': 'Gorilla',
            'H': 'Hear', 'I': 'In', 'J': 'Joke', 'K':'Kind', 'L':'Lame', 'M':'Money', 'N':'None','O':'Open',
            'P': 'Proper', 'Q':'Quartile', 'R':'Run','S':'Sure','T':'Tire','U':'Under','V':'Vehicle','W':'Wire',
            'X':'Xylophone','Z':'Zoo'}

def notoalphabet(name):
    name = name.upper()
    new_list = [phonetic.get(item) for item in name]
    return new_list

print(notoalphabet('Angelina'))


