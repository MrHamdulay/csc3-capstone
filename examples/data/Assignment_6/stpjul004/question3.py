""" Independent Electoral Commission voting progam
 Author: Julius Stopforth (STPJUL004)
 Date: 2014-04-23 """

print("Independent Electoral Commission")
print("-"*32)

# Collect votes
done = False

print("Enter the names of parties (terminated by DONE):")
votes = []
while not done:
    vote = input("")
    if vote == 'DONE':
        done = True
    else: 
        votes.append(vote)

votes.sort()

#count the votes and display result
print("\nVote counts:")
while len(votes) > 0:
    print("{:<10}".format(votes[0]),"-",votes.count(votes[0]))
    votes = votes[votes.count(votes[0]):]