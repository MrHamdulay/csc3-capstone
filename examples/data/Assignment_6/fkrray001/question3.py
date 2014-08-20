# Author : Rayaan Fakier FKRRAY001
# Date : 21 - 04 2014
# question3.py
''' Program which count votes per political party '''

def main():
    print("Independent Electoral Commission")
    print("--------------------------------")
    print("Enter the names of parties (terminated by DONE):")
    
    # Initiating/empty variables
    parties = ""
    parties_list = []
    parties_dict = {}
    
    # Takes entries of parties and adds them to an unordered list
    while parties != "DONE":
        parties = input()
        parties_list.append(parties)
    parties_list.remove("DONE")
    
    # Takes the parties from the list and counts their 'votes', storing in a dictionary
    for party in parties_list:
        if not party in parties_dict:
            parties_dict[party] = 1
        else:
            parties_dict[party] += 1
    
    # Creates a list of parties (single entries) to be alphabetized
    party_alph_list = []
    for party1 in parties_dict:
        party_alph_list.append(party1)
    party_alph_list.sort()
    
    # Prints a result of the votes in a pseudo-table
    print("\nVote counts:")
    #table = "{0}{1:>10} {2}" [tried ... failed]
    for party2 in party_alph_list:
        votes = parties_dict[party2]
        spaces = len(party2)
        print(party2 + " " * (10 - spaces), "-", votes)
    
main()