print('Enter strings (end with DONE):')
inp = input()
strings = []
while(inp != "DONE"):
    strings.append(inp)
    inp = input()

already_printed  = set()
print('\nUnique list:')
for word in strings:
    if word in already_printed:
        continue
    print(word)
    already_printed.add(word)
