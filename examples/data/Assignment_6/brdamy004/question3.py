# Assignment 6 question 3
# Amy Brodie
# 24/04/2014

print("Independent Electoral Commission")
print("--------------------------------")
party_votes = {}
votes = 0

# get user input and store first value
name = input("Enter the names of parties (terminated by DONE):\n")
if name != "DONE":
   party_votes[name] = 0

# count votes and store in a dictionary
while name != "DONE":
   if name in party_votes:
      party_votes[name] += 1
   else:
      party_votes[name] = 1
   name = input()
   
print()
print("Vote counts:")
if party_votes:   
   for a in sorted(party_votes):
      print("{0:<10}".format(a), "-",party_votes[a])
   