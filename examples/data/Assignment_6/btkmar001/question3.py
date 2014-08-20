# question3.py
# A program that counts votes
# Martin Batek
# BTKMAR001
# 22 April 2014

print("Independent Electoral Commission")
print("--------------------------------")
votes = []
names = ""

print("Enter the names of parties (terminated by DONE):")
while names != "DONE":
    names = input("")
    if names != "DONE":
        votes.append(names) # creates a list of votes

parties = []

for vote in votes:
    if vote not in parties:
        parties.append(vote) # creates a list of parties
        
parties.sort() # arranges list of parties alphabetically

print()
print("Vote counts:")
for party in parties:
    print(party+((len("Vote counts")-len(party))*" ")+"-", votes.count(party))
    # counts the votes that each party on the party list has on the vote list