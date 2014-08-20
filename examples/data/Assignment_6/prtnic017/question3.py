# Student Number: PRTNIC017
# Date: 4/22/14

parties = []
print('Independent Electoral Commission')
print('--------------------------------')
party = input('Enter the names of parties (terminated by DONE):\n')
while party != 'DONE':
    if party not in (parties[i][0] for i in range(len(parties))):
        parties.append([party, 1])
    else:
        for i in range(len(parties)):
            if parties[i][0] == party:
                parties[i][1] += 1
                break

    party = input('')

parties = sorted(parties)

print('\nVote counts:')
for i in range(len(parties)):
    print("%-10s" % parties[i][0], '-', parties[i][1])