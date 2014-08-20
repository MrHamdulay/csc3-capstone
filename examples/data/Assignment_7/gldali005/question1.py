#module of utility functions to manipulate 2-dimensional arrays of size 4x4
#Ali Goldstein
#30 april 2014

#prompt the user to enter in strings
strings=input("Enter strings (end with DONE): \n")
list=[]
new=[]

#going through the list and when a item is not in the list, add it to the new list
while strings!="DONE":
    list.append(strings)
    strings = input("")
    for i in list:
        if not i in new:
            new.append(i)

#print the new list       
print("")
print("Unique list:")
for i in new:
    print(i)

        