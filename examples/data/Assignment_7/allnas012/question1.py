#Nasiha Ally
#ALLNAS012
#02 May 2014





x = input ("Enter strings (end with DONE):\n")
mylist=[]

while x != 'DONE':
    mylist.append(x)
    x = input("")
    
    duplicate = []
    for i in range(len(mylist)):
        for j in range(i+1,len(mylist)):
            if set(mylist[i]) == set(mylist[j]):
                duplicate.append(j)
                if x=="DONE":
                    break                
    
    duplicate = sorted(set(duplicate))
    
    newlist= [mylist[i] for i in range(len(mylist)) if i not in duplicate]

print()
print("Unique list:")
newlist= [mylist[i] for i in range(len(mylist)) if i not in duplicate]
for i in newlist:
    print(i)
    
