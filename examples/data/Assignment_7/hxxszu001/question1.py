#Annie Ho
#Counting votes

lst=[]
name=input("Enter strings (end with DONE):\n")
while name != "DONE":
    lst.append(name)
    name=input("")

names=[]
for name in lst:
    if name not in names:
        names.append(name)

print()
print("Unique list:")
for j in names:
    print(j)
