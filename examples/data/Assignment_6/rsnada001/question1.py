strings = []
print('Enter strings (end with DONE):')
readstring = input()
while (readstring != 'DONE'):
    strings.append(readstring)
    readstring = input()
if len(strings) != 0:
    length = len(max(strings, key=len))
print('\nRight-aligned list:')
for i in range(len(strings)):
    print('{:>{}}'.format(strings[i], length))
