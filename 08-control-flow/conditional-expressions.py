zip_code = '54321'

if len(zip_code) == 5:
  check = 'Valid'
else:
  check = 'Invalid'

print(check)


check = 'Valid' if zip_code.isnumeric() else 'Invalid'

print(check)