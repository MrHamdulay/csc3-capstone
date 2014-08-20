print('Independent Electoral Commission')
print('--------------------------------')
print('Enter the names of parties (terminated by DONE):')

word = ''
arrP = []


while word != 'DONE':
    word = input('')
    arrP.append(word)     
    
print('')    
print('Vote counts:')    

y = arrP.index('DONE') 
del arrP[y]

#Sort
arrP.sort()

arrP.append('')

count = 1
string = ''

for k in range(1,len(arrP)):
    if arrP[k - 1] == arrP[k]:
        count += 1
        continue
    else :
        string = "{0:<10} - " + str(count)
        print(string.format(arrP[k - 1]))
        #print(arrP[k - 1], count)
        count = 1