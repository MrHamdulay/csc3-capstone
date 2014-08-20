#Get parties
parties = {}
print("Independent Electoral Commission")
print("--------------------------------")
print("Enter the names of parties (terminated by DONE):")
inp = input()
while inp != "DONE":
    if inp in parties:
        parties[inp] += 1
    else:
        parties[inp] = 1
    inp = input()

#Print results
print("\nVote counts:")
for k,v in sorted(parties.items(), key = lambda x: x[0]):
    print(k + " "*(11 - len(k)) + "- %d" % v)
