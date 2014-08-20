#MZWNIC001/Nicholas Mazower    
#24/04/2014
#Vote counter



vote=input("Independent Electoral Commission\n--------------------------------\nEnter the names of parties (terminated by DONE):\n")
votes=[vote]
parties=[vote]
#t is a dummy variable to start the while loop, it has no external significance
t=1
while t>0:
    if vote =="DONE":
        #these two operations are necessary to remove 'DONE' from the parties and votes lists
        votes.remove("DONE")
        parties.remove("DONE")
        break
    else:
        vote=input("")
        if vote not in parties:
            parties.append(vote)
        votes.append(vote)
parties=sorted(parties)
print("\nVote counts:")
for a in parties:
    count=votes.count(a)
    count=str(count)
    count="- " + count
    width=13-len(a)
    print(a,'{:>{width}}'.format(count,width=width))
