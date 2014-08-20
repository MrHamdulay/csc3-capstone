#Assignment 6, Question 3
#Avreyna Kistensamy
#20 April 2014

print("Independent Electoral Commission")
print("--------------------------------")

ballot = []
parties = input("Enter the names of parties (terminated by DONE):\n")
while parties != 'DONE':
    ballot.append(parties)
    parties = input("")
    
#dictionary entries    
vote_count = {}
for party in ballot:
    if not party in vote_count:
        vote_count[party] = 0
    vote_count[party] += 1
    
Alpha_VC = sorted(vote_count.keys())
print()
print("Vote counts:")
for key in Alpha_VC:
    print(key, "-".rjust(11-len(key)),vote_count[key])
    