zip_code = '12345'

if len(zip_code) == 5 and zip_code.isnumeric():
  check = 'valid'
else:
  check = 'Invalid'

print(f"{zip_code} is a {check} zip code in the USA.")