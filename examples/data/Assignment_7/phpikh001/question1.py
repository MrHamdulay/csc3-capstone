#Ikhlaas Pohplonker
#27 April 014
# a program where the user can enter a list of strings and these strings are then printed in the same order but without duplicates
strings=input("Enter strings (end with DONE):\n")
list_of_strings=[]
while strings!="DONE":#asks user to enter a string until the string equals down
    if not strings in list_of_strings:#adds string to list_of_strings if the string is not in the list_of_strings
            list_of_strings.append(strings)    
    strings=input()
print()
print("Unique list:")
for i in list_of_strings:
    print(i)
    
