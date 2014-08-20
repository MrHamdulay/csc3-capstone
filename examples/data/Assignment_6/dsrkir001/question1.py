#Program where the user can enter a list of strings followed by the sentinel
#20 April 2014
#Kiran Desraj

#empty list
names = []     

#get list of names

name = input('Enter strings (end with DONE):\n')
    
while name != 'DONE':     #use 'DONE' as sentinel
    names.append(name)
    name = input('')

print("")
print('Right-aligned list:')

if names == []:
    print('')



else:                         
    longestword = max(names, key=len)    #finds the length of longest string  
    length = len(longestword)    
    for name in names:     
        print ((length - len(name))*' ',name, sep='')    #prints names  