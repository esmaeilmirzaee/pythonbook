# Method: A function that acts upon a specific object
laptop = 'Apple Mac book pro'

print(laptop.find('A'))
print(laptop.find('Ap'))
print(laptop.find('p'))
print(laptop.find('o'))
print(laptop.find('o', -1))
print(laptop.find('o', 4, 8))
print(len(laptop))
print(laptop.find('P'))

print(laptop.index('A'))
print(laptop.index('b'))