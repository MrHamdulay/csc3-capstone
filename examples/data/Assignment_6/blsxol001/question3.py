# a program to count the number of votes
# Xola GcwaBE
# 26/04/2014
# BLSXOL001

print("Independent Electoral Commission")
print("--------------------------------")
print("Enter the names of parties (terminated by DONE):")
party=" "                       # initializing party
votes =[]                       # initializing votes - empty list
while party!="DONE":            # setting sentinel = 'DONE'
    party=input()               # get party the user votes for
    votes.append(party)         # adding each party voted for into votes
x = votes.index("DONE")         # finding the index of the sentinel
del votes[x]                    # deleting sentinel from list
print()
print("Vote counts:")
vpp = []                        # intialize votes per party (vpp)
for vote in votes:              
    if vote in vpp:             # check if vote is in votes per party
        vote = 0    
    else:
        vpp.append(vote)        # if not, add it tio the list: vvp
vpp.sort()                      
for i in vpp:                   # sorting the vpp list alphabetically
    print("%-10s - %s" % (i, votes.count(i)))   
