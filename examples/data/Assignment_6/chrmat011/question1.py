print('Enter strings (end with DONE):')
string = input('')
strings = []
long = 0

while string != 'DONE':
    if len(string) > long:
        long = len(string)
    strings.append(string)
    string = input('')

print('\nRight-aligned list:')
for i in strings:
    print(' '*(long-len(i)),i,sep='')
