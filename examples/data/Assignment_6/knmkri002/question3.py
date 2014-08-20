"""Program to count the number of votes per political party
Kristin Kinmont
20 April 2014"""

#print heading
print("Independent Electoral Commission")
print("-"*32)

#get votes
vote = input("Enter the names of parties (terminated by DONE):\n")
votes = []
while vote != "DONE":
    votes.append(vote)
    vote = input("")
print()
    
#create a party dictionary and count the votes
parties = {}
for i in votes:
    if i not in parties:
        parties[i] = 0
    # counting votes
    parties[i] +=1

#sort parties
parties_list = sorted(parties)
    
#print out votes for each party
print("Vote counts:")
for i in parties_list:
    party = '{0:<10}'.format(i)
    print(party,"-",parties[i])