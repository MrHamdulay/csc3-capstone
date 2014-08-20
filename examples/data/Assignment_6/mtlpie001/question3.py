#piet motalaota
print("Independent Electoral Commission")
print("--------------------------------")

elections = [] 


party = input("Enter the names of parties (terminated by DONE):\n")

elections.append(party) 

while "DONE" not in party:
    party=input("")
    elections.append(party)

elections.remove("DONE")

for i in range(len(elections)):
    partyvotes = elections.count(elections[i])
elections=sorted(elections)

dic_election={}
for party in elections:
    if party not in dic_election:
        dic_election[party]=1
    else:
        dic_election[party]+=1
counts = []
for x in elections: 
    if [x,dic_election[x]] not in counts :
        counts.append([x,dic_election[x]])
print('\nVote counts:')
for i in range(len(counts)):
            
    print('%10s - %d'%(counts[i][0].ljust(10),counts[i][1])) 
