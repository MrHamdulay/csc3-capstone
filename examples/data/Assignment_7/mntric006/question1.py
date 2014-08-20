#input
newstring = ""
liststrings = []
print("Enter strings (end with DONE):")
while newstring != "DONE" :
    newstring = input()
    liststrings.append(newstring)
liststrings.pop()

uniquelist = []
for i in liststrings:
    if i not in uniquelist:
        uniquelist.append(i)

print("")
print("Unique list:")
for j in uniquelist: print(j)