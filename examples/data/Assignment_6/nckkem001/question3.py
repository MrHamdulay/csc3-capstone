"""Program to count votes for political parties
Kemeshan Naicker
23 April 2014"""

def vote_counter():
    
    print("Independent Electoral Commission")
    print("--------------------------------")
    #Prompt user for votes.
    print("Enter the names of parties (terminated by DONE):")
    party=input()
    #Set accumulator list variables.
    parties=[]
    total_parties=[]
    #Store all inputs and simultaneously and separately store only names that have not yet been stored.
    while party != "DONE":
        parties.append(party)
        if party not in total_parties:
            total_parties.append(party)
        party=input()
    #Create a new list with the party names formatted to field width ten and votes for each part stored along side.
    vote_tally=[]
    for i in total_parties:
        vote_tally.append("{0:10} - ".format(i)+str(parties.count(i)))
    #Sort and output list.
    vote_tally=sorted(vote_tally)
    print("\nVote counts:")
    for i in vote_tally:
        print(i)
        
if __name__=="__main__":
    vote_counter()
    