# Default arguments: Fallback arguments that are passed to a function if an explicit value is not provided for a parameter

def add(a = 0, b = 0):
  return a + b

print(add())
print(add(13))
print(add(1, 3))
print(add(b = 3))
print(add(b = 1, a = 3))