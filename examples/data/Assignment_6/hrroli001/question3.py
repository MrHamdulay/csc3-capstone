# Question 3 - Assignment 6
# Oliver Harrison
# 21 April 2014


# Print Intro

print("Independent Electoral Commission")
print("--------------------------------")

# Get votes

votes = []

vote_input = input("Enter the names of parties (terminated by DONE):\n")

while vote_input != "DONE":
    votes.append(vote_input)
    vote_input=input("")\
        
        


# Sort

vote_count=[]

votes = sorted(votes)             # a, a, a , b , b , c 

# Count

x=-1
previous = ""

for i in votes:
    if i != previous:
        vote_count.append(1)
        x += 1
    else:
        vote_count[x] = vote_count[x] + 1
    previous = i


# Format and Pring

votes_clean=[]
previous = 0
for i in votes:
    if i != previous:
        votes_clean.append(i)
    else:
        continue
    previous = i
    
print("")
print("Vote counts:")
for i in range(len(votes_clean)):
    print(votes_clean[i], (11-(len(votes_clean[i])))*" ", "- ",  vote_count[i], sep = "")
    
    

