"""print with no duplicates
Vahin Gounden
27-04-2014"""

#get input
strings = input("Enter strings (end with DONE):\n")

#make lists
stringlst = []
if strings != "DONE":
    stringlst = [strings]
    dstring = []

#set up sentiniel and add to list
while strings != "DONE":
    strings = input()
    if strings != "DONE":
        stringlst.append (strings)

print()
print("Unique list:")

#remove duplicates
for j in stringlst:
    if j not in dstring:
        print(j)
        dstring.append (j)
            
