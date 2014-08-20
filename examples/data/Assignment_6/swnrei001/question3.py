"""Question 3 of assignment 6
Count votes of parties in an election 
SWNREI001
20/04/2014"""

def votecounter(votes):
    """Counts the number of votes per party in 'votes', returns a dictionary:
    format: {<party name>:<number of votes>}"""
    party_votes = {}
    for i in votes:
        if i in party_votes.keys():
            party_votes[i] += 1
        else:
            party_votes[i] = 1
    return party_votes

def main():
    """Main function of module
    Gets an inputted list of votes for parties, counts votes
    Outputs as sorted list"""
    title = "Independent Electoral Commission"
    print(title)
    print('-' * len(title))
    s = input("Enter the names of parties (terminated by DONE):\n")
    votes = []
    while s != "DONE":
        votes.append(s)
        s = input()
    print()
    print("Vote counts:")
    counted = votecounter(votes)
    for i in sorted(counted):
        print(i.ljust(10) + " - " + str(counted[i]))
        
if __name__ == "__main__":
    main()