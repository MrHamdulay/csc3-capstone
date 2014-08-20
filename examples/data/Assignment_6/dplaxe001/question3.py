'''Vote counter program
Axel du Plessis
20-04-2014'''

partys = []
partyVotes = {}

print("Independent Electoral Commission")
print("--------------------------------")
print("Enter the names of parties (terminated by DONE):")

party = input("")
form = "{0:<11}"
while party != "DONE":
    if party in partys:
        partyVotes[party] = partyVotes[party] +1
    else:
        partyVotes[party] = 1
        partys.append(party)
        
    party = input("")
  
partys.sort()
print("\nVote counts:")
for party in partys:
    print(form.format(party)+ "- "+str(partyVotes[party]))