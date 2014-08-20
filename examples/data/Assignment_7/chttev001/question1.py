"""Tevin Chetty
30 April 2014
Program to find unique words in a string"""

strings=[] #Creates a new list

string=input("Enter strings (end with DONE): \n") 

while string!= "DONE" : #A list of all the inputs
    strings.append(string)
    string=input("")

strings_unique=[] #creates a new list with only unique words
for string in strings:
    if string not in strings_unique:
        strings_unique.append(string)
    else:
        continue

print()
print("Unique list:")

for i in strings_unique:
    print(i)