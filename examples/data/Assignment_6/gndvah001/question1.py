"""right align a list of strings
Vahin Gounden
22-04-14"""

#get input
names = input("Enter strings (end with DONE):\n")

#make lists
namelst = []
if names != "DONE":
    namelst = [names]

x = 0
#set up sentiniel and add to list
while names != "DONE":
    names = input()
    if names != "DONE":
        namelst.append (names)
        lngstname = (max(namelst, key = len))
        x = len(lngstname)


print()
print("Right-aligned list:")

#print right aligned list using longest name
for j in namelst:
    print("{0:>{width}}".format(j, width = x))