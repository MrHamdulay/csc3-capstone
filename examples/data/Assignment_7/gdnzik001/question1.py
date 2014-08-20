"""program to print strings entered by the user in the same order but without duplicates
Zikho Godana
27 April 2014"""

#ask the user for strings
string=input("Enter strings (end with DONE):\n")

#create an empty list of the strings
strings=[]
strings2=[]

#add the strings entered by the user to the list
while string!="DONE":
    strings.append(string)
    string=input("")
print()
print("Unique list:")

for string in strings:
    #create another list of the unique strings
    if string not in strings2:
        strings2.append(string)
        print(string)
    