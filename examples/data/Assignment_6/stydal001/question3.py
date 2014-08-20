# Program to count the votes for political parties in an election
# Dalise Steynfaard
# STYDAL001
# 26 April 2014

def i_e_c():
    """Gets parties from user and counts votes for each party"""
    parties = {}
    
    print("Independent Electoral Commission")
    print("--------------------------------")
    party = input("Enter the names of parties (terminated by DONE):\n")
    
    while party != 'DONE':
        if party:
            if not(party in parties):
                parties[party] = 1
            else:
                parties[party] += 1
                    
        party = input('')
    
    parties2 = sorted(list(parties.keys()))    
    
    if len(parties) > 0:
        print("\nVote counts:")
        
        for i in parties2:
            print(i.ljust(10) + ' -', parties[i])
              
i_e_c()