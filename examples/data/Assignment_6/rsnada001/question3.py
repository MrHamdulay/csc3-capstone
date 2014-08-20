print('''Independent Electoral Commission
--------------------------------
Enter the names of parties (terminated by DONE):''')
parties = []
votes = []
party = input()
while(party != 'DONE'):
    if not party in parties:
        parties.append(party)
    votes.append(party)
    party = input()
parties = sorted(parties)
print('\nVote counts:')
for i in range(len(parties)):
    print('{:<{}}{}'.format(parties[i],10,' - ' + str(votes.count(parties[i]))))
