inputs=[]
name=input("Enter strings (end with DONE):\n")
while name != "DONE":
    inputs.append(name)
    name=input("")

unique=[]
for name in inputs:
    if name not in unique:
        unique.append(name)

print()
print("Unique list:")
for i in unique:
    print(i)