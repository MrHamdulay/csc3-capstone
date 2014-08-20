"""nasha somoina meoli
24th april 2014
program to count votes"""

def countthevotes():
    print("Independent Electoral Commission")
    print("--------------------------------")
    #toget the parties
    x = input("Enter the names of parties (terminated by DONE):\n")
    parties = [x]
    votes = [x]
    while x != "DONE":
        x = input("")
        if x != "DONE":
            votes.append(x)
        if x in parties or x == "DONE":
            continue
        parties.append(x)
    # to arrange the parties in alphabetical oreder
    parties.sort()
    print()
    print("Vote counts:")
    a = 0
    if parties!= ["DONE"]:
        for i in parties:
            numberofvotes = 0
            vote = votes.count(i)
            numberofvotes+=(vote)
            print(parties[a]," "*(10-len(parties[a]))+"-",numberofvotes) 
            a+=1
countthevotes()
