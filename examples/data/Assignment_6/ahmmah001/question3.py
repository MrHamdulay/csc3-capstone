'''Program to count votes of each political party
Mahnoor Ahmed
23 April 2014'''

partylist=[]
reflist=[]
count=0
print("Independent Electoral Commission")
print("-"*32)
party=input("Enter the names of parties (terminated by DONE):\n")      #adding each party name to a list
partylist.append(party)
while party != "DONE":
    party=input("")                                      
    partylist.append(party)
    
del partylist[-1]                                                      #deleting DONE from list
partylist.sort()
print("\nVote counts:")
for i in partylist:   
    count=partylist.count(i)                                           #counting votes for each party
    if i not in reflist:                                               #adding party name to a new list to make sure no party names are duplicated
        reflist.append(i)
        print("{0:<10}".format(i)," - ",count,sep="")