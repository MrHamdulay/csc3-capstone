'''List of strings entered and printed in same order without duplicates
Inga Ndyoki
02 May 2014'''

names = []
name = input("Enter strings (end with DONE):\n\n")
if name != 'DONE':
    names.append(name)

while name != 'DONE':
    flag = 'false'
    for i in range(len(names)):     #this loop checks if the next string entered exists in the list already
        if names[i] == name:
            flag = 'true'
    if flag == 'true':      #if the string exists then it doesn't add it to the list
                i = i
    else:
        names.append(name)
    name = input()
print('Unique list:')
for i in range(len(names)):
    print(names[i])