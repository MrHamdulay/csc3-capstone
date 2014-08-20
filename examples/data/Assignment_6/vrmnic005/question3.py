#VRMNIC005
#Assignment 6 question 3

def parties():
    """ counts the number of votes per party"""
    print("""Independent Electoral Commission
--------------------------------""")
    party_list = {}
    new_vote = input("Enter the names of parties (terminated by DONE): \n")
    while new_vote!= "DONE":
        if new_vote in party_list:  #check if party already has votes
            party_list[new_vote] += 1
        else:
            party_list[new_vote] = 1    #creates key for new party
        new_vote = input()
        
    sorted_parties = sorted(party_list.keys())

    print("\nVote counts:")
    for party in sorted_parties:
        print("{0:<10}".format(party), "-", party_list[party])

parties()
