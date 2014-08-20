


ListOfNames=[]
name=input("Enter strings (end with DONE):\n")
while name!="DONE":
    ListOfNames.append(name)
    name=input("")
length=0
for i in range(len(ListOfNames)):
    if len(ListOfNames[i])>length:
        length=len(ListOfNames[i])


    
print("\nRight-aligned list:")
for j in range(len(ListOfNames)):
    j=ListOfNames[j]
    print(j.rjust(length))