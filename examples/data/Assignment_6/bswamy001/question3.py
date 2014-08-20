"""Amy Bosworth, Assignment 6, Question 3, program to count the number of votes for political parties in an election"""

print("Independent Electoral Commission")
print("--------------------------------")

# Get political parties
vote=input("Enter the names of parties (terminated by DONE):\n")
votes={}

# Creates dictionary of political parties and no. of votes
while vote!= 'DONE':
  if vote in votes:
    votes[vote]+=1
  else:
    votes[vote]= 1
  vote=input()
    
# make political parties a sorted list
pparties= list(votes.keys())
pparties= sorted(pparties)

# print vote counts
print("\nVote counts:")

for i in pparties:
  space=11-len(i)
  print(i,(space*' '),'- ',votes[i],sep='')
  
