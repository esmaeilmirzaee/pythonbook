zip_code = '12345'

if len(zip_code) == 5 and zip_code.isnumeric():
  check = 'valid'
else:
  check = 'Invalid'

print(f"{zip_code} is a {check} zip code in the USA.")

if 'a' < 'b' < 'c':
  print('What')

if 'a' < 'b' and 'b' < 'c':
  print("somehow")

if 1 < 2 < 3:
  print(True)

if 1 < 2 and 2 < 3:
  print("Got it")