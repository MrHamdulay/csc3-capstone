"""vote counter
Carla Wilby
19 April 2014"""

#get names and add to array
parties = []
vote = input("Independent Electoral Commission\n--------------------------------\nEnter the names of parties (terminated by DONE):\n")
while vote != "DONE":
    parties.append(vote)
    vote = input("")

#count and return votes
party_and_tally = [[]]
counted_parties = []
print("\nVote counts:")
for i in parties:
    while i not in counted_parties:
        tally = parties.count(i)
        a = "{0:10}".format(i)
        party_and_tally.append([a, tally])
        counted_parties.append(i)
        
#sort and return final tally        
party_and_tally.sort()
for i in range(1,len(party_and_tally)):
    print(party_and_tally[i][0],"-",party_and_tally[i][1])