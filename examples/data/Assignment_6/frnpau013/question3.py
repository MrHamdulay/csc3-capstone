"""vote counter"""

print("Independent Electoral Commission\n--------------------------------")

# creating and adding to a dictionary of votes, plus an alphabetically sorted list of party names
print("Enter the names of parties (terminated by DONE):")
party = ""
votes = {}
while party != "DONE":
    party = input()
    votes[party] = votes.get(party, 0) + 1
del votes["DONE"]
partylist = sorted(votes)


# printing out results
print()
print("Vote counts:")
for i in partylist:
    print("{0:10} -".format(i), votes[i])