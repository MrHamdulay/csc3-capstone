# Lehlogonolo Masetla
#20 April 2014

""" This programme allows the user to enter a list of names and the print them out right justified"""

names = [] # introduces an empty list

name = input("Enter strings (end with DONE):\n") #Asks the user for a name

santinel = "DONE" # for when the user is done listing

name.lower() # changes all names to lower case
name.capitalize() # capitalize the first letters of names
width = len(name)
while name != santinel:
    
    names.append(name) # Adds each name into the array
    name = input("")    
    
    if len(name)>width:
        width = len(name) # Keeps the length of the longest name
        
print("")       
print("Right-aligned list:")

for i in range(len(names)):
    name_items = names[i]
    print(name_items.rjust(width)) # prints out the list right justified with the width of the longest name