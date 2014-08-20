strings = []

inp = input('Enter strings (end with DONE):\n')
while(inp != 'DONE'):
    if not inp in strings:
        strings.append(inp)
    inp = input('')

print('\nUnique list:')
for i in strings:
    print(i)
