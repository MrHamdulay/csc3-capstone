print("Independent Electoral Commission")
print("--------------------------------")
userInput = input("Enter the names of parties (terminated by DONE):\n\n")
if(userInput != "DONE"):
    votes = []
    length = 0
    
    while(userInput!="DONE"):
        votes.append(userInput)
        length+=1
        userInput = input("")
    
    numVotes = [0]
    parties = [votes[0]]
    #removes repititions in votes to make an array with all parties
    for j in votes:
        partyDetected = False
        for k in parties:
            if(partyDetected == False):
                if(j == k):
                    partyDetected =True
        if(partyDetected == False):
            parties.append(j)
            numVotes.append(0)
            
            
    parties = sorted(parties)            
    #counts votes for each party
    count = 0
    for i in range(len(parties)):
        for j in votes:
            if(j == parties[count]):
                numVotes[count] += 1
        count+=1
    #print(votes)
    #print(parties)
            
    print("Vote counts:")
    count=0
    for i in parties:
        print(i," "*(10-len(i))," - ",numVotes[count],sep="")
        count+=1
else:
    print("Vote counts:")
