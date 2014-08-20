# This program counts the number of votes for each political party in an election.
# The program accepts a sequence of names of parties (terminated by the word DONE)
# The votes per party are then printed in acsending order

# Student Name: Simeon Nandjembo

# Student Number: NNDSIM001

# 22 April 2014

print("Independent Electoral Commission\n--------------------------------")

party = input("Enter the names of parties (terminated by DONE):\n")
rawlist = [] # store party names
rawdict = {} # store party votes
sortdict = [] # store sorted dictionary keys

# Store strings to the dictonary
while party != "DONE":
    rawlist.append(party)
    party = input()

# Store voters counts in the dictionary
for i in rawlist:
    if not i in rawdict:
        rawdict[i] =0 # initialize the dictionary with new keys and value of 0
    rawdict[i] += 1 # add new value at each occurance of the key

# sort the dictionary by converting its keys into a list
for key in rawdict:
    sortdict.append(key)
sortdict.sort()

# print out dictinary keys in a column on width 10 and their corresponding votes
print("\nVote counts:")
for j in sortdict:
    print("{0:<11}- {1}".format(j,rawdict[j]))

#Sample I/O:

#Independent Electoral Commission
#--------------------------------
#Enter the names of parties (terminated by DONE):
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
#DONE

#Vote counts:
#apples     - 2
#bananas    - 2
#kiwis      - 1
#oranges    - 5
#pears      - 1