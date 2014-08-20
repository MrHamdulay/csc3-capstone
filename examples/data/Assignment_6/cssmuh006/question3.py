import collections 
print("Independent Electoral Commission\n--------------------------------\nEnter the names of parties (terminated by DONE):\n")
party={}
pt=""
while(pt!="DONE"):
    pt=input()
    included=False
    for i in party:
        if(i==pt): #determine if party is already in dictionary and add 1 to vote count if found
            party[i]+=1
            included=True
    if( not included and pt!="DONE"): # if party is not in dicionary add it in with votes=1
        party[pt]=1

party = collections.OrderedDict(sorted(party.items())) #sorting dictionary
print("Vote counts:")
for i in party:
    print(i," "*(11-len(i)),"- ",party[i],sep="") # displaying output