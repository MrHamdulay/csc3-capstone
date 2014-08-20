x = []
X =input("Enter strings (end with DONE):\n")
while X != "DONE":
    x.append(X)
    X=input("")
x.reverse()
for i in x:
    while x.count(i) > 1:
        x.remove(i)
x.reverse()
print("\nUnique list:")
for j in x:
    print(j)