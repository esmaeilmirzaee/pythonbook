# Parameter: a name for an expected argument to a function
# Argument: the actual value passed as an input to a function
# Sequential argument: an argument passed sequentially, in order
# Keyword argument: an argument whose parameter name is explicitly written out
# Default argument: Fallback value provided to a parameter if the user does not specify one
# print(*objects, sep='', end='\n', file=sys.stdout, flush=False)
print('ABC', 'DEF')
print('ABC', 'DEF', sep='!')
print('ABC', 'DEF', sep='--*--')
print('ABC', 'DEF', sep='!', end='')
print('ABC', 'DEF', sep='!', end='\t', flush=True)
print('ABC', 'DEF', sep='!', end='\n')


print('ABC', 'DEF', sep='**', end='#')
print('ABC', 'DEF', end='#', sep='**')


