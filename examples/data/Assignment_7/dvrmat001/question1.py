names=[]
name=input("Enter strings (end with DONE):\n")
while name != "DONE":
    names.append(name)
    name=input("")

awesome=[]
for name in names:
    if name not in awesome:
        awesome.append(name)

print()
print("Unique list:")
for i in awesome:
    print(i)
