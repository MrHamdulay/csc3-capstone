"""question 3
Assignment 6
Micaela Menegaldo"""

#need to sort answer

def votes():
    votes={}
    party=""
    while party != "DONE":
        party=input("")
        if party not in votes:
            votes[party]=1
        elif party in votes:
            votes[party]+=1
    del votes["DONE"]
    print()
    print("Vote counts:")
    for i in sorted(votes):
        print(i," "*(11-len(i)),"- ",votes[i],sep="")
    

if __name__=='__main__':
    print("Independent Electoral Commission\n--------------------------------\nEnter the names of parties (terminated by DONE):")
    votes()