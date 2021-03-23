print('1234 5678 9')
print('1234 5678 9'.replace(' ', '-'))
print('1234 5678 9'.replace(' ', '--'))
print('1234 5678 9'.replace(' ', ''))
print('1234 5678 9'.replace(' ', ', '))
print('1234 5678 9'.replace(' ', 'abcdef'))

phone_number = '123 456 789 0'
print(phone_number.replace('1', '13579'))
print(phone_number)

phone_number = phone_number.replace('1', '13579')
print(phone_number)