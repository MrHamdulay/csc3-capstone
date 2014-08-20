L=[]

print("Enter strings (end with DONE):")
s=input()
if s != "DONE":
    L.append(s)
while s != "DONE":
    s=input()
    if s != "DONE":
        if not s in L:
            L.append(s)
print()
print("Unique list:")
for i in L:
    print(i)
    