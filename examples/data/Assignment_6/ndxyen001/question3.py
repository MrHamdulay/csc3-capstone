# Yentl Naidu (NDXYEN001)
# 24 April 2014
# Assignment 6
# Question 3

# Create empty list
p = []

# Get the input
parties = input("Independent Electoral Commission\n--------------------------------\nEnter the names of parties (terminated by DONE):\n")

# Create loop to get the list of parties with a sentinel 
x = 0
while parties != 'DONE': 
    p.append(parties)
    parties = input('')
    if (len(parties)) <= 10:
        x = len(parties)
    else:
        break

# Start with zero votes
vote = {}

# Count parties and add new parties as they are encountered
for parties in p:
    if not parties in vote:
        vote[parties] = 1
    else:
        vote[parties] += 1
   
# Print a statement showing the vote counts       
print("\nVote counts:")

# Print out votes
for parties in sorted(vote): # sort out votes using the "SORT FUNCTION"
    print (parties.ljust(10),"-", vote[parties])  
        


    
    
    