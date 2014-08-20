'''A program where the user can enter a list of strings and these strings are then printed in the same order but without duplicates.
fadzai mupfunya
29/04/14'''

#for storing the string enterd in a list
strings=input("Enter strings (end with DONE):\n")
the_list=[]
while strings != "DONE":
    if strings not in the_list:  #to check if item enterd is already in the list
        the_list.append(strings)
    strings=input()
   
print()   
print("Unique list:")

#to print out the new list  of strings in the same order but with no duplicates
for string in the_list: 
    print(string)

