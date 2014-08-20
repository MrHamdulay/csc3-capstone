#Ashton Singh   
#25 April 2014
#Voting System

#Creating Empty list
votes = []

#Getting party names
print("Independent Electoral Commission\n--------------------------------")

party = input("Enter the names of parties (terminated by DONE):\n").lower()

#Populating lists
while party != "done":
    exists = False
    for i in range (len(votes)): 
        if party in votes[i]: #Testing if a party exists
            votes[i][1] += 1 #Adding to number of votes
            exists = True 
            
    if not exists: #Appending new party if it does not already exist in list
        votes.append([party, 1])
    party = input().lower()

   
print("\nVote counts:")
votes.sort() #sort list

for i in range (len(votes)):
    r = "{0:<10}".format(votes[i][0]) #Format column with 10 spaces
    print(r, "-",votes[i][1])
        
    
    
    
