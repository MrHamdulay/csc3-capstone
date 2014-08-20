
votes_no = [] #list of number of votes(empty list)

print("Independent Electoral Commission\n--------------------------------")#name of the election runners

party_name = input("Enter the names of parties (terminated by DONE):\n").lower()#names of paties being voted for

#counting the votes
while party_name != "done":
    exists = False
    for i in range (len(votes_no)): 
        if party_name in votes_no[i]: 
            votes_no[i][1] += 1
            exists = True 
            
    if not exists: 
        votes_no.append([party_name, 1])
    party_name = input().lower()

   
print("\nVote counts:")#output of the program
votes_no.sort() 

for i in range (len(votes_no)):
    r = "{0:<10}".format(votes_no[i][0]) 
    print(r, "-",votes_no[i][1])
        
    
    
    
