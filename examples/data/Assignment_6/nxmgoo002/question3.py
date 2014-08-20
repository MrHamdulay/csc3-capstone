'''program for Independent Electoral Commission
Nxumalo Goodman
22 April 2014'''

def elections():
    #creates a dictionary and a list
    votes = {}
    no_votes = 0
    vote_name = []
    
    
    print("Independent Electoral Commission")
    print("--------------------------------")
    name = input("Enter the names of parties (terminated by DONE):\n")
    while name != 'DONE':
        if name not in vote_name:
            vote_name.append(name)
        if name in votes:
            votes[name] += 1
        else:
            votes[name] = 1
            no_votes += 1
        name = input("")
        
    #prints out the output
    vote_name.sort()
    print()
    print("Vote counts:")
    for i in vote_name:
        print(i," "*(9-len(i)),"-",votes[i])
    
elections()