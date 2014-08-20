#Program to enter a list of strings which are printed without duplicates
#27 April 2014
#Kiran Desraj



#Get list
string = input('Enter strings (end with DONE):\n')
strings = []

while string != 'DONE':       #use 'DONE' as sentinel
    strings.append(string)
    string = input('')

print('')      #Prints empty line


strings2 = []    
    
    
print('Unique list:')
for string in strings:
    if not string in strings2:    #Check if item is in strings2
        strings2.append(string)    #moves item to strings2
        print(string)

    
