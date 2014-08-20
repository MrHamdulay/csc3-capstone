'''removing duplicates from a string program
nic findlay
27 april 2014'''
i = 0
words = []
word = ''
print('Enter strings (end with DONE):')

while word != 'DONE':
    word = input('')
    words.append(word)
    i += 1
    
del words[i-1]  #removes done

no_duplicates = []
for i in words:
    if i in no_duplicates:
        continue
    else: 
        no_duplicates.append(i)
        
print('\nUnique list:')
for i in no_duplicates:
    print(i)