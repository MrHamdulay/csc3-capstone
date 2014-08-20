"""Question 1, Assignment 6
Tejasvin Bagirathi BGRTEJ001"""

name_list = []
print('Enter strings (end with DONE):')
print()
name = input()
name_len = 0
#Loop for user input of names
while name != 'DONE':
    name_list.append(name)
    if len(name) >= name_len:
        name_len = len(name)
    name = input()
#Declare list to store new names 
new_names = []
print('Right-aligned list:')

#Get name to equal length by adding spaces
for y in name_list:
        while len(y) != name_len:
            y=" "+y
        if len(y)==name_len:
            new_names.append(y)

#Print names            
for c in new_names:
    print(c)
            
#for i in range(0, len(name_list)):
    #spaces = name_len-len(name_list[i])
    #print((spaces)*' ', name_list[i], sep='')
    
        
        
        
        