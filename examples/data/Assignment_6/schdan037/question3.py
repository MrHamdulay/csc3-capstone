"""Daniel Schwartz
SCHDAN037
question 3
april 2014"""


def main():
    """main"""
    print("Independent Electoral Commission")
    print("--------------------------------")

    # receives input of parties
    parties = []

    party = input("Enter the names of parties (terminated by DONE):\n")

    while party != "DONE":
        parties.append(party)
        party = input("")

    # count votes
    votes = {}
    for party in parties:
        if party not in votes:
            votes[party] = 0
        votes[party] += 1

    #print votes
    print()
    print("Vote counts:")
    sorted_votes = votes.keys()
    sorted_votes = sorted(sorted_votes)

    for vote in sorted_votes:
        vote_str = "{0:<10} - {1}"
        print(vote_str.format(vote, votes[vote]))

# runs main on entry
if __name__ == '__main__':
    main()