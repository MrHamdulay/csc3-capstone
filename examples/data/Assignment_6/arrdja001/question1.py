"""Assignment 6 Question 1
25 April 2014
Djavan Arrigone"""

strings = input("Enter strings (end with DONE): \n")
names = [] #initialises the list.


while strings != ("DONE"):#this conditional loop appends users entries in to list.
    names.append(strings)
    strings = input("")
    
count = 0
for i in range(len(names)): #this conditional loop determines which of the strings within the list has the longest length
    if len(names[i]) > count:
        count = len(names[i])
print()   
print("Right-aligned list:")

for j in names:
    print(j.rjust(count))
