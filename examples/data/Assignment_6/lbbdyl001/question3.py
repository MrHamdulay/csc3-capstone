"""
Voting Poll
"""
print("Independent Electoral Commission\n--------------------------------")
poll=input("Enter the names of parties (terminated by DONE):\n")

votes=[] #empty list

while (poll != "DONE"): #end when "DONE" is entered
    votes.append(poll) #append input to votes    
    poll = input()

party_name=[]

for party in range (len(votes)): #to create list of parties
    if(votes.index(votes[party])==party):
        party_name.append(votes[party]) 

party_name.sort()        
count=[]

for i in party_name:
    count.append(0)

for i in range(len(party_name)):
    for party in range(len(votes)):
        if(votes[party]==party_name[i]):
            count[i]+=1 #counts number of votes
print()            
print("Vote counts:")

for i in range(len(party_name)):
    print("{0:<11}- {1}".format(party_name[i],count[i])) #format field length 10
    
