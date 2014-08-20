# Program to count number of votes for each party
# Danielle Sher

from collections import Counter
print("Independent Electoral Commission")
print("--------------------------------")
strlist = []
x = input("Enter the names of parties (terminated by DONE):\n")

if x != "DONE":
    while True:
        if x != "DONE":
            strlist.append(x)
            x = input("")
        elif x == "DONE":
            break
    
    votes = Counter(strlist)

    keys = votes.keys()
    values = votes.values()

    sparty = " ".join(keys)
    lparty = sparty.split()            # list of names
    snum = " ".join("{0}".format(n) for n in values)
    lnum = snum.split()                # list of numbers

    width = (max(map(len, strlist))) # length of longest party name
    print()
    print("Vote counts:")

    newlist = []
    j = 0
    for i in range(len(lparty)):
        x = lparty[j] + " "*(11-len(lparty[j])) + "-" + " " + lnum[j]
        j = j + 1
        newlist.append(x)
    newlist.sort()

    for i in newlist:
        print (i)
    
elif x == "DONE":
    print()
    print("Vote counts:")
    
    
    
   



    