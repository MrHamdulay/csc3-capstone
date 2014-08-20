#piet motalaota
print("Independent Electoral Commission")
print("--------------------------------")

votes = [] 


party = input("Enter the names of parties (terminated by DONE):\n")

votes.append(party) 

while "DONE" not in party:
    party=input("")
    votes.append(party)

votes.remove("DONE")

for i in range(len(votes)):
    partyvotes = votes.count(votes[i])
votes=sorted(votes)

dic_part={}
for party in votes:
    if party not in dic_part:
        dic_part[party]=1
    else:
        dic_part[party]+=1
        
        
Total_votes = []
for x in votes: 
    if [x,dic_part[x]] not in Total_votes :
        Total_votes.append([x,dic_part[x]])
print('\nVote counts:')
for i in range(len(Total_votes)):
            
    print('%10s - %d'%(Total_votes[i][0].ljust(10),Total_votes[i][1])) 
