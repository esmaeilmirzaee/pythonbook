def add(a, b, c):
  print("The sum of three numbers is", a + b + c)

add(5, 4, 3)
add(5, 4, c = 3)
add(5, b = 4, c = 3)

# SyntaxError
# add(c = 10, 4, 5)
# add(c = 10, a = 2, 2)