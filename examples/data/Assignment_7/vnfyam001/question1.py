XString=input("Enter strings (end with DONE):\n")
Slist=[]
NonReplicatedList=[]
Stored=""
while XString != "DONE":
    Stored=Stored+" "+XString
    XString=input("")
Stored=Stored[1:]    
Slist=Stored.split(" ")

for i in range(len(Slist)):
    if Slist[i] in NonReplicatedList:
        continue
    else:
        NonReplicatedList.append(Slist[i])
print("\nUnique list:")        
for i in range(len(NonReplicatedList)):
    print(NonReplicatedList[i])

        