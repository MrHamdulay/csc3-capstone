# Program to eliminate duplicates in a list
# Danielle Sher

strlist = []
x = input("Enter strings (end with DONE):\n")
if x != "DONE":
    while True:
        if x != "DONE":
            strlist.append(x)
            x = input("")
        elif x == "DONE":
            break

s = []
for i in strlist:
    if i not in s:
        s.append(i)

newlist = "\n".join(s)

print()
print("Unique list:")
print (newlist)
