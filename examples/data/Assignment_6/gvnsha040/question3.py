print("Independent Electoral Commission\n--------------------------------")

party = []

parties = input("Enter the names of parties (terminated by DONE):\n")

while parties != "DONE": 
   
    party.append(parties)    
    parties = input("")
party.sort()

vote={}

for x in party: 
    
    if x not in vote: 
        vote[x]=1
    else:
        vote[x]+=1 
        
print("\nVote counts:")

for x in sorted(vote):
    print("{0:10}".format(x),"-",vote[x])