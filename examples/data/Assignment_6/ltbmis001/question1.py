name=input("Enter strings (end with DONE):\n")
names=[name]

for i in names:
    if name=="DONE":
        break
    else:
        name=input("")
        names.append(name)

del names[-1]

k = len(names)
j=0
c=0

while j<k:
    
    if len(names[j])>c:
        c=len(names[j])
    else:
        c==c

    j+=1
print("\nRight-aligned list:")
 
for i in names:
    gap = " "*(c-len(i))
    print(gap+i)

