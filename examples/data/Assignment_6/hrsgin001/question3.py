#Gina Horscroft
#Assignment6

arrVote = []
votes = input("Independent Electoral Commission\n--------------------------------\nEnter the names of parties (terminated by DONE):\n")
while (votes!= "DONE"):
    arrVote.append(votes)
    votes = input("")
arrVote.sort()
prev = ""
parties = []
voteParties = []
pos = -1
for i in range(len(arrVote)):
    #if the party name is new - create a new vote space
    if (arrVote[i] != prev):
        prev = arrVote[i]
        parties.append(arrVote[i])
        voteParties.append(0)#creates new vote space - to store votes for individual parties
        pos+=1
    voteParties[pos] += 1
    
print("\nVote counts:")
for a in range(len(parties)):
    #prints out parties with width=10
    print(parties[a], " "*(10-len(parties[a])), " - ", voteParties[a], sep = "")