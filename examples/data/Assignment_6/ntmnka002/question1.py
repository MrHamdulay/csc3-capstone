arrName = []
word = ''
maxWord = 0

print('Enter strings (end with DONE):')

while word != 'DONE':
    word = input('')
    arrName.append(word)
    if len(word) > maxWord:
        maxWord = len(word)
    
length = len(arrName)

print()
print('Right-aligned list:')

for k in range(len(arrName) - 1):
    string = "{0:>" + str(int(maxWord)) + "}"
    out = string.format(arrName[k])
    print(out)
    
       # out = "{0:>" + str(int(height)) + "}"