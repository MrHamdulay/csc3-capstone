""" a program to calcuale the number of votes per political party
nelisile mkhwebane
23/04/2014"""

print ("Independent Electoral Commission")
print ("-"*32)

""" get the vote from the citizen"""
votes = []
vote = input("Enter the names of parties (terminated by DONE):\n")

""" they should enter until "DONE" is entered"""
while vote != "DONE":
    votes.append(vote)
    vote = input("")
    
""" to get a list of different words """
counts= {}
for w in votes:
    counts[w] = counts.get(w,0)+1
    #print (counts[w])
    
""" getting the different parties voted for"""

unique_parties = list(counts.keys())
#print (unique_parties)

""" sorting unique words in alphabetical order"""
unique_parties.sort()

"""printing out the two columns of words and counts"""
print("")
print("Vote counts:")
for w in unique_parties:
    print("{0:<10}{1:>3}{2:>1}".format(w,"- ",counts[w]))

