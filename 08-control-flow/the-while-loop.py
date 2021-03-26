# loop: a series of instructions that is repeated.
count = 0

while count < 100:
  print(count)
  count+=10

correct = True

secret_number = random(1, 100)

while correct:
  print(secret_number)
  a = int(input("Guess the number"))
  if a == secret_number:
    print("You guessed it.")
    correct = False
  else:
    print("Try again")

