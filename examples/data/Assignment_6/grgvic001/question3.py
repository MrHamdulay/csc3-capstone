#program to collect party names and count votes for each entered party
#victor gueorguiev
#20 april 2014

def main():
    xinput = ''
    party_names = []
    votetally = []
    print('Independent Electoral Commission')
    print('--------------------------------')
    xinput = input('Enter the names of parties (terminated by DONE):\n')
    while xinput != 'DONE':
        if not xinput in party_names:
            party_names.append(xinput)
            votetally += [1]
        else:
            votetally[party_names.index(xinput)] += 1
        xinput = input('')
    finalscore = []
    for i in range(len(party_names)):
        finalscore.append([party_names[i],votetally[i]])
    finalscore.sort()
    print('\nVote counts:')
    for i in range(len(party_names)):
        print(('{0:<10}').format(finalscore[i][0]),' - ',finalscore[i][1],sep='')
main()        