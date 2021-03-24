def simple_calculator(num_1: int, num_2: int, oper: str):
  if oper == '+':
    print(num_1 + num_2)
  elif oper == '-':
    print(num_1 - num_2)
  elif oper == '*':
    print(num_1 * num_2)
  elif oper == '/':
    print(num_1 / num_2)
  else:
    print('Please check the provided inputs.')

simple_calculator(1, 2, '+')
simple_calculator(1, 2, '-')
simple_calculator(1, 2, '/')
simple_calculator(1, 2, '*')

simple_calculator(1, 2, 2)
