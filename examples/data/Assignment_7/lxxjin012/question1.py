#a program where the user can enter and print a list of strings in the same order
#Jenny Luo
#29 April 2014

#add string as an input from the user into a list
strings=[]
string=input("Enter strings (end with DONE):\n")
while string != "DONE":
    strings.append(string)
    string=input("")

#add items into new list
liststrings=[]
for i in strings:
    if i not in liststrings:
        liststrings.append(i)
    else:
        pass

#print out the list of strings
print()
print("Unique list:")
for i in liststrings:
    print(i)

