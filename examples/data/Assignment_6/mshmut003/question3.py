'''Program to the IEC count votes
Mutali Mashamba
24 April 2014'''

def slot ():
    doc = """Independent Electoral Commission
--------------------------------"""
    print (doc)
    # Prompt user to enter party names
    party = input("Enter the names of parties (terminated by DONE):\n")
    # Create empty list for parties
    parties = []
    # Add all the entries into the list of parties
    while party != "DONE":
        parties.append(party)
        party = input('')
    # Create empty dictionary to keep track of each parties vote-count
    votes = {}
    # Add parties into dictionary (from the list)
    for i in parties:
        # enters the party into dictionary
        if i:
            votes.update({i:0})
        # if party already exists in dictionary, go to the next one
        elif i in votes:
            pass
    for i in parties:
        for j in votes:
            if i == j:
                # Compares list of parties with dictionary, increases count in the dictionary (value) each time the party appears in the list
                votes[j] += 1
    # Printing the results
    maxi = 10
    print ('\nVote counts:')
    for i in sorted(votes):
        print (i,' '*(maxi-len(i))+'-',votes[i])
    # Be Happy
        
slot()
