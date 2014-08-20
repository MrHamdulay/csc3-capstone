"""Assignment 6 question 3 Count votes
Ross van der Heyde VHYROS001
20 April 2014"""

from collections import OrderedDict

print("Independent Electoral Commission\n--------------------------------")
parties = {}

# read in vote, add to dictionary
vote = input("Enter the names of parties (terminated by DONE):\n")

while vote != "DONE":
    if vote in parties:
        parties[vote]+=1
    else: # if name is not in the dictionary, add it with one vote
        parties[vote]=1
    vote = input()

#print names, number of votes
d = OrderedDict(sorted(parties.items()))#Create orderedDict to store sort dict
                
print("\nVote counts:")
output = "{:10}"
for i in d:
    print(output.format(i), "-", d[i])
    
#OrderedDict(sorted(d.items()) also works

#apples
#oranges
#oranges
#oranges
#pears
#bananas
#bananas
#kiwis
#oranges
#apples
#oranges