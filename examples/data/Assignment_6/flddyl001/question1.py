list = []

x = ""
print("Enter strings (end with DONE):")

previousmax = 0

while x != "DONE":
    
    x = input()
    if x == "DONE":
        break
    list.append(x)

    if len(x)>previousmax:
        previousmax=len(x)

print()
print("Right-aligned list:")

for i in range(len(list)):
    print(" "*(previousmax - len(list[i])),list[i],sep="")
