'''Write a Python program where the user can enter a list of strings and 
these strings are then printed in the same order but without duplicates.
Sinead Urisohn
27 April 2014
'''
#get string
name=input("Enter strings (end with DONE):\n")
#set list
names=[]
#loop until sentinel
while name!="DONE":
    #get unique names
    if name not in names:
        names.append(name)
    name=input("")
#output list of strings
print("\nUnique list:")
for n in names:
    print(n)