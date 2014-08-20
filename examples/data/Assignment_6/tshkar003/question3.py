#TSHKAR003

print("Independent Electoral Commission\n--------------------------------")
parties=[]
name=input("Enter the names of parties (terminated by DONE):\n")
while name != "DONE": 
    parties.append(name)    
    name=input("")
parties.sort()
votes={} 
for name in parties: 
    if name not in votes: 
        votes[name]=1
    else:
        votes[name]+=1 
print("\nVote counts:")
for name in sorted(votes):
    print("{0:10}".format(name),"-",votes[name])
    
