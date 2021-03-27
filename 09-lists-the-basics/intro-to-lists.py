# List: a data structure that stores an ordered sequence of objects.
# List is an array in other programming languages.
empty = []
print(empty)

empty = list()
print(empty)

cars = ["Honda Civic", "Mazda 6", "Lexus 2020"]
print(cars)
print(len(cars))

grades = [3.8, 3.9, 3.2, 3.5]
print(grades)

for element in grades:
    if element > 3.0:
        print('A')
    elif element <= 3.0 and element > 2.5:
        print('B')
    elif element <= 2.5 and element > 2:
        print('C')
    elif element <= 2:
        print('D')
    else:
        print('Check provided grade')
