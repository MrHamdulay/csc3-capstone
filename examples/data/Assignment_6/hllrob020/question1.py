names = [] #empty list to store strings
length_names = [] #empty list to store length of strings

name = input('Enter strings (end with DONE):\n') #prompt user to input names
while name != 'DONE' or name != 'done': #loop repeats while input not done
    if name == 'done' or name == 'DONE': #for no input (boundary condition)
        break
    else:
        names.append(name) #for each iteration store the string in names
        length_names.append(len(name)) #for each iteration store the length of the string in length_names
        name = input() #so user can press return and enter new string on new line
        if name == 'done' or name == 'DONE': #if user has no more input, done ends loop
            break
if names == []: #for boundary condition of no input
    print()
    print('Right-aligned list:')
    print()
else:
    longest = length_names[0] #to determine length of longest string
    for i in range(len(length_names)): #to iterate through length_names list
        if length_names[i] > longest:
            longest = length_names[i]

    print()        
    print('Right-aligned list:')   
    for j in range(len(names)): #to print right-aligned list
        print(' '*(longest-len(names[j])),names[j],sep = '') #prints spaces multiplied by difference in 'len' of string j and longest string   