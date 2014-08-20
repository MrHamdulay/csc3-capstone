#Calculations with vectors
#Keanon Fell
#24 April 2014

print("Independent Electoral Commission")
print("--------------------------------")
print("Enter the names of parties (terminated by DONE):")

vote = ""
parties = []
while vote != "DONE":
    vote = input()
    if len(vote) <= 10 and vote != "DONE":
        parties.append(vote)

ballot = []
for i in range(len(parties)):
    if not parties[i] in ballot:
        ballot.append(parties[i])
        
ballot.sort()

voting=[]
for i in range(len(ballot)):
    sum = 0
    for j in range(len(parties)):
        if ballot[i] == parties[j]:
            sum+= 1
    voting.append(sum)
    
print()
print("Vote counts:")      
for i in range(len(ballot)):
    print(ballot[i] , (10 - len(ballot[i]))*" " , " - " , voting[i],sep="")