#ASSIGNMENT 7
#QUESTION 1
#NLTWES001

namelist=[]
print("Enter strings (end with DONE):")
while (True):
    name=input()
    if name=="DONE":
        break
    else:
        namelist.append(name)
    
newlist=[]
for i in namelist:
    if i not in newlist:
        newlist.append(i)

print()
print("Unique list:")
for j in newlist:
    print(j)
        