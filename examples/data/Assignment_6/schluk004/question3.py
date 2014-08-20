names=[]
votes=[]
dict1={}
found=False
flag=0

print("Independent Electoral Commission\
\n--------------------------------")

party=input("Enter the names of parties (terminated by DONE):\n")

while(party!="DONE"):
    
    for i in range(len(names)):
        if names[i]==party:
            found=True
            flag=i
            
    if found==False:
        names.append(party)
        votes.append(0)
        flag=len(names)-1
        
    votes[flag]+=1
    party=input()
    found=False

for i in range(len(names)):
    dict1[names[i]]=votes[i]

snames = sorted(names)

print("\nVote counts:")
for i in range(len(names)):
    print(snames[i]," "*(11-len(snames[i])),"- ",dict1[snames[i]],sep="")