print("Independent Electoral Commission")
print("--------------------------------")
print("Enter the names of parties (terminated by DONE):")
print()
election_results = {}
party = ""
while party != "DONE":
    party = input()
    if party == "DONE": break
    if (party in election_results) == False:
        election_results [party] = 1
    else:
        election_results [party] += 1
    
print("Vote counts:")
for party in sorted(election_results):
    print(party + " "*(11 - len(party)) + "-", election_results[party])