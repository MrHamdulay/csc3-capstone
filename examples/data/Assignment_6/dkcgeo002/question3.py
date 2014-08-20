__author__ = 'George de Kock'
""" Count Votes
    2014-4-20   """

print("Independent Electoral Commission","--------------------------------",sep = "\n")
parties = []
votes = {}
print("Enter the names of parties (terminated by DONE):\n")
while True:
    party = input("")
    if party == "DONE":
        break
    if not party in parties:
        parties.append(party)
        votes[party] = 1
    else:
        votes[party] += 1

parties.sort()
print("Vote counts:")
for a in parties:
    x = "{0:<10} - {1}".format(a,votes[a])
    print(x)