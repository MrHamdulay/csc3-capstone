# Luke Henkeman
# HNKLUK001
# 25 April 2014
# question3.py
# count votes in election

print("Independent Electoral Commission")
print("--------------------------------")
def rawvotes():
    name = input("Enter the names of parties (terminated by DONE):\n")
    rawvotes = [name]
    while name != "DONE":
        name = input("")
        if name != "DONE":
            rawvotes.append(name)
        else:
            break
#    print(rawvotes)
    votenum = len(rawvotes)
#    print(votenum)
    parties = [rawvotes[0]]
    for i in range(1,votenum):
        if rawvotes[i] in parties:
            continue
        else:
            parties.append(rawvotes[i])
        i+=1
    parties.sort()
#    print(parties)
    numparties = len(parties)
    print("\nVote counts:")
    for i in range(numparties):
        result = rawvotes.count(parties[i])
        gap = (9-len(parties[i]))*" "
        print(parties[i],gap,"-",result)
        i+=1
    
rawvotes()