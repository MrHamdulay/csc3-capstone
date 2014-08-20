#kereshnee pillay
#voting
# 24 April 2014

#empty list
votes = []
#Get party names
print("Independent Electoral Commission\n--------------------------------")

party = input("Enter the names of parties (terminated by DONE):\n").lower()

#fill into list
while party != "done":
    exists = False
    for i in range (len(votes)): 
        if party in votes[i]: #check if a party exists
            votes[i][1] += 1 #Add one to number of votes
            exists = True 
            
    if not exists: #Append new party if it does not currently exist in list
        votes.append([party, 1])
    party = input().lower()

   
print("\nVote counts:")
votes.sort() #sort list

for i in range (len(votes)):
    r = "{0:<10}".format(votes[i][0]) #format with column with 10
    print(r, "-",votes[i][1])
        
    
    
    
