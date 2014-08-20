"""Counts votes for the election
Adam Oosthuizen
"""
votes=[]
print("Independent Electoral Commission\n--------------------------------")

parties = input("Enter the names of parties (terminated by DONE):\n")
#create party list
partyList = []
if parties != "DONE":
    while parties != "DONE":
        partyList.append(parties)
        votes.append(0)
        parties = input()
    
    temp = set(partyList)
    partyReal = list(temp)
    partyReal.sort()
    
    for i in range (len(partyReal)):
        c = 0
        for j in range(len(partyList)):
            if partyReal[i] == partyList[j]:
                c+=1
                votes[i] = c
                     
        
    print("\nVote counts:")
    
    for i in range (len(partyReal)):
        print(partyReal[i], " "*(9-len(partyReal[i])), "-", votes[i])
else:
    print("\nVote counts:")
    ##print data
    #length = len(distinct_parties)
    
    #print("\nVote counts:")
    
    #c = 0
    #for y in range (0, length-1):
        #print(distinct_parties[y], " "*(9-len(distinct_parties[y])), "-", votes[y])
        #c = y+1
    #print(distinct_parties[c], " "*(9-len(distinct_parties[c])), "-", votes[c])

#else:
    #print("\nVote counts:")

