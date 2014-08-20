"""Assignment 7 Question1 question1.py
2 May 2014 Djavan Arrigone"""

s = input("Enter strings (end with DONE): \n")
l = []

while s != "DONE": #This sentinel loop continues until users entry is "DONE"
    if s not in l: #This boolean statement establishes if user entry already in list. 
        l.append(s) #If the users entry in not in the list, it is now appended to list
    s = input("")

print()
print("Unique list:")

for i in l:
    print(i)
