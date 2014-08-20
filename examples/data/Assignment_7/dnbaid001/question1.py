#Assignment 7 - Question 1
#Prints list of strings without duplicates
#Aidan de Nobrega
#27/04/2014

strings = []

string = input("Enter strings (end with DONE):\n")
while string != "DONE":
    if string not in strings: #only appends to list of not already in list
        strings.append(string)
    string = input()
    
print("\nUnique list:")

for string in strings:
    print (string)
