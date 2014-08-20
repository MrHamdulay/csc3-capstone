print("Independent Electoral Commission\n--------------------------------")

votes = []

#User is prompted to enter the political party/parties they want to vote for
vote = input("Enter the names of parties (terminated by DONE):\n")
while vote != 'DONE':
    votes.append(vote) # This appends/adds the vote(s) the user types in, to votes
    vote = input("")

counters={}

# This calculates the total number of votes towards a certain political party
for vote in votes:
    if not vote in counters:
        counters[vote]=0
    counters[vote] += 1
    
sorted_parties = sorted(counters.keys())

print("\n""Vote counts:")
for vote in sorted_parties:
    print(vote + ' '*(10 - len(vote)) ,'-',counters[vote])
    
