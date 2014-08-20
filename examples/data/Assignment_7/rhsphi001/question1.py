'''Phillip Ruhesi
01/05/2014
this program prints a list of words without duplicated'''

x=input('Enter strings (end with DONE):\n')

words=[]                 #Empty list
words.append(x)          #Add input to list
while x!='DONE':
    x=input('')          
    if x not in words:   #check if the word has been added yet
        words.append(x)       
    else:
        continue
         
del words[len(words)-1]  
print('\nUnique list:')
for j in words:
    print(j)
