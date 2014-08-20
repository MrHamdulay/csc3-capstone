"""Program to remove duplicate values (Question 1)
27 April 2014
Jaren Hendricks"""

# Empty lists 
newStrings = []
Strings = []

#Headings
print("Enter strings (end with DONE):")

# Adds strings to lists and breaks when user enters 'DONE'
while True:
    s = input()
    if s == "DONE":
        break
    else:
        Strings.append(s)

# Headings
print ()
print ("Unique list:")

# Saves the first appearance of a value/string in a seperate array
for i in Strings:
    if i not in newStrings:
        newStrings.append(i)

# Outputs the array
for j in newStrings:
    print(j)

