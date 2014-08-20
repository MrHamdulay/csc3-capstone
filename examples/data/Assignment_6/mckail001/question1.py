"""Assignment 6 question 1: Right allign list of names
Ailsa Mackay MCKAIL001
2014-04-22"""

list_of_names = []
name = input("Enter strings (end with DONE):\n")
while name != "DONE":
    list_of_names.append(name) #name is appended to the list if it is not the sentinel
    name = input("") 
    
longest = len(list_of_names[0])
for i in list_of_names:
    if len(i) > longest: #finds the length of the longest word
        longest = len(i)

print("")
print("Right-aligned list:")
for i in list_of_names:
    print(" "*(longest - len(i)), i, sep="")
    