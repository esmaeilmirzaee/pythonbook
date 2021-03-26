# Recursion: when a function calls itself 
def lift_off_in(num):
  if num <= 0:
    return
  print(f"Lifting off in {num} seconds.")
  lift_off_in(num - 1)

lift_off_in(10)

def fibonacci(num):
  if num <= 1:
    return 1
  else:
    return fibonacci(num - 1) + fibonacci(num - 2)

print(fibonacci(3))