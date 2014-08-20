"""program to eliminate duplicates in strings 
joshua gullan
27 april 2014"""

original=[]
unique=[]

x=input("Enter strings (end with DONE):\n")

while x!="DONE":
    original.append(x)    #creates list of strings
    x=input()

if x=="DONE":
    for i in original:  #gets rid of duplicates
        if i in unique:
            continue
        else:
            unique.append(i)
            
print("\nUnique list:")
for i in unique:  #prints unique list
    print(i)

    