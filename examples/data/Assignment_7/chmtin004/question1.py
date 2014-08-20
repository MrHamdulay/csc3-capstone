"""Program to return a list with no duplicates
Tinotenda Chemvura CHMTIN004
29 April 2014"""

#___________________Program Starts Here____________________

#create empty list

strings = []

#obtain list of strings from user

name = input("Enter strings (end with DONE):\n")
if name != "":
    strings.append(name)
    
    
if len(name) > 0:
    while name != "DONE":
        name = input()
        strings.append(name)
    
    #remove the "DONE" from the list
    
    del strings[-1]
    
    #create new empty list and add the strings but ommiting the duplicates
    
new_list = []
for i in strings:
    if i not in new_list:
        new_list.append(i)
        
#print the new list of strings

print("\nUnique list:")
for j in new_list:
    print(j)
    
#_______________________Program ends here______________________________