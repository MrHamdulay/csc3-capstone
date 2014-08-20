"""A program to count the number of votes for each party
Alison Hoernle
HRNALI002
20 April 2014"""

print("Independent Electoral Commission")
print('-'*32)

list = []

#get list of parties

party = input("Enter the names of parties (terminated by DONE):\n")
while party != 'DONE':
    list.append(party)
    party = input("")
print()
print("Vote counts:")
# sort the list alphabetically
list.sort()
    
# count the number of votes for each party
vote_count = []
for party in list:
    if party not in vote_count:
        num_votes = list.count(party)
        vote_count.append(party)
        print(party.ljust(10), '-', num_votes)
    
    