def reversed(str):
  first_index = 0
  last_index = len(str) - 1
  temp_word = ''

  while last_index >= first_index:
    temp_word += str[last_index]
    last_index -= 1

  return temp_word

def reverse(word):
  if len(word) <= 1:
    return word
  return word[-1] + reverse(word[:-1])

print(reversed('Palindroma'))
print(reverse('Hello'))