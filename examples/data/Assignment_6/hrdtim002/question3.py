"""program to count votes
Tim Hardie
23-4-14"""

if __name__ == '__main__':
    print ("Independent Electoral Commission\n--------------------------------")
    
    #user inputs names and ends with sentinel value of DONE
    name_in = input ("Enter the names of parties (terminated by DONE):\n")
    names_list = []
    while (name_in != 'DONE'):
        names_list.append (name_in)
        name_in = input()
    names_list.sort()
    
    #lists to store party names and corresponding votes
    party_list = []
    votes = []
    for party in names_list:
        if party not in party_list:
            party_list.append(party)
    for i in range (len (party_list)):
        votes.append (0)
        
    #count votes
    for party in names_list:
        for i in range (len (party_list)):
            if (party == party_list[i]):
                votes[i] += 1
    
    #print results
    print ("\nVote counts:")
    for i in range (len (party_list)):
        print('{0:10}'.format(party_list[i]), "-", votes[i])