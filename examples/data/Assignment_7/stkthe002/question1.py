#Thea Sitek, STKTHE002
#18.05.2012
#Remove duplicates, sorted as before

words = input('Enter strings (end with DONE): \n')

#creare list
array = []
while words != 'DONE':
    array.append(words)
    words = input()

#create new list, remove duplicates
new = []
for e in array:
    if e not in new:
        new.append(e)

print('\nUnique list:')

#display
for i in new:
    print(i)