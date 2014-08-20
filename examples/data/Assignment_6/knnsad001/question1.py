#Program where the user can enter a list of strings followed by the sentinel
#knnsad001
#question1

#introducing empty list
names = []     

#this will get the list of names

name = input('Enter strings (end with DONE):\n')  #introducing name variable

while name != 'DONE':     #this will use 'DONE' as a sentinel
    names.append(name)
    name = input('')

print("")
print('Right-aligned list:')

if names == []:
    print('')

else:                         
     
    length = len(longestword)    
    for name in names:     
        print (name, sep='')    #prints names  