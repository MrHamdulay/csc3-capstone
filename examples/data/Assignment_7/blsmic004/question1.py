''' program where the user can enter a list of strings and these strings 
are then printed in the same order but without duplicates
Michele Balestra  BLSMIC004
30 April 2014'''

# Get strings from user and create empty list
strings = input("Enter strings (end with DONE):\n")
strlist = []

# add each string supplied by user to list
while strings != 'DONE':
    strlist.append(strings)
    strings = input()
  
# Create empty list to store unique words
unique = []  

# Add each unique word to list in order user supplied
for i in strlist:
    if i not in unique:
        unique.append(i)
  
# Prints each unique word in order supplied by user
print("\nUnique list:")      
for j in unique:
    print(j)