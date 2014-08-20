'''program where the user can enter a list of strings and prints in order without duplicates
sankara mallane
27 april 2014'''

# empty list
Strings = []

# get the strings from user and place in list
xString = input("Enter strings (end with DONE):\n")
while xString != 'DONE':
    Strings.append (xString)
    xString = input("") 

# start with an empty Dictionary
stringDictionary = {}

# add strings in list to dictionary
for xString in Strings:
        stringDictionary[xString] = 0

#print unique list
print()        
print('Unique list:')

#print out list in order without duplicates
for xString in Strings:
    if stringDictionary[xString]==0:
        print(xString)
        stringDictionary[xString]=1 

