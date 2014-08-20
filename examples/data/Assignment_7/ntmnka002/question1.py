arrX = []
arrN = []
word = ''

print('Enter strings (end with DONE):')

while word != 'DONE':
    word = input('')
    arrX.append(word)
    
    if not word in arrN:
        arrN.append(word)
        
print()
print('Unique list:')

#y = arrN.index('DONE')
#del arrX[y]

for k in range(len(arrN) - 1):
    print(arrN[k])