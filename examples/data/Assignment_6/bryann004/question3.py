#Anna Borysova
#ass6,q3
#2014-04-22

print("Independent Electoral Commission")
print("--------------------------------")
print("Enter the names of parties (terminated by DONE):")
parties = {}
party = ""
while True:
    party = input("")
    if party == "DONE":
        break
    if party in parties:
        parties[party] += 1
    else:
        parties[party] = 1
print("\nVote counts:")
for key in sorted(parties):
    print ("{:<10}".format(key) + " - " + str(parties[key]))