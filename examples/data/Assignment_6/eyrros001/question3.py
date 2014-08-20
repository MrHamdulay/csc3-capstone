"""count the number of votes for each political party in an election
Ross Eyre
20/April/2014"""

print("Independent Electoral Commission\n--------------------------------")

name = str(input("Enter the names of parties (terminated by DONE):\n"))
#create party list
parties = []

if name !='DONE':
#get more names and append to list
    while name != 'DONE':
        parties.append(name)
        name = str(input())
        
    
    #create distinct party list
    parties_set = set(parties)
    
    distinct_parties = list(parties_set)
    distinct_parties.sort()
    
    #count number of occurences of party names
    votes = []
    for i in range (0, len(distinct_parties)):
        votes.append(parties.count(distinct_parties[i]))
        
    #print data
    length = len(distinct_parties)
    
    print("\nVote counts:")
    
    c = 0
    for y in range (0, length-1):
        print(distinct_parties[y], " "*(9-len(distinct_parties[y])), "-", votes[y])
        c = y+1
    print(distinct_parties[c], " "*(9-len(distinct_parties[c])), "-", votes[c])

else:
    print("\nVote counts:")