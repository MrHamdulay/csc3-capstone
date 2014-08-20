x=input("Enter strings (end with DONE):\n")

words2=[]
while x!="DONE":
    words2.append(x)
    x=input("")
print()

print("Right-aligned list:")
for word in words2:
    print("{0:>}".format(word))

