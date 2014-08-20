# Yudhi Moodley
# Voting evaluator
# 23/04/2014

parties = {} 

def voting():
    party = ''
    print("Independent Electoral Commission")
    print("--------------------------------")
    print("Enter the names of parties (terminated by DONE):")
    
    while party != 'DONE': # sentinel
        party = input()
        if party in parties:
            parties[party] += 1
        else:
            parties[party] = 1
            
    del parties['DONE'] # remove sentinel form list
    print('')
    print("Vote counts:")


    for i in sorted(parties): # sorts the list in alphabetical order
        length = 10-len(i) 
        print(i + " "*length + " - " + str(parties[i]))
        
voting()