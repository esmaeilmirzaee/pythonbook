# \t    tab
# \n    carriage return
# \\    print backslash
# \' or \"    print single/double quote inside a single/double quote text
print('This is a \ttab.')
print('This is a \nnew line.')
print('\'To be or not to be\'')
print("\"To be or not to be\"")

file = r"C:\\Program Files\\Python3.8.0\\bin\\python.exe"
print(file)

# Raw string
file = r"C:\\Program Files\\Python3.8.0\\bin\\python.exe"
print(file)

a_file_location_and_file_name_could_be_long = ''
so_when_you_want_to_code = ''
you_can_break_the_line_to_improve_readability = ''

sentence = a_file_location_and_file_name_could_be_long + \
            so_when_you_want_to_code + \
            you_can_break_the_line_to_improve_readability

print(sentence)