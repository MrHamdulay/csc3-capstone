# program to count number of party votes in an election
# by Jacob Mwanza
# 22/04/201


# enter the party votes
def elections():
    party_votes = {}
    votes = ''
    # enter votes
    print ('Independent Electoral Commission')
    print ('--------------------------------')    
    print("Enter the names of parties (terminated by DONE):")
    while votes != 'DONE':
        votes = input()
        if votes != 'DONE':
            if votes in party_votes:
                party_votes[votes] = party_votes[votes] + 1
            else:
                party_votes[votes] = 1
            
    print()
    print('Vote counts:')
    
    formatted_data = ('{:<10} - {}')
    key = sorted(party_votes.keys())
    vote = sorted(party_votes.values())
    for i in key:
        print(formatted_data.format(i,party_votes[i]))
    
    

elections()    




