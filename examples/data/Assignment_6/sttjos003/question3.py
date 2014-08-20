#Election program
#Joe Sutton
#23 April 2014

print("Independent Electoral Commission\n--------------------------------\nEnter the names of parties (terminated by DONE):")
listofvotes=[] #create empty list
vote=input("")

while not vote=="DONE":
    listofvotes.append(vote)
    vote=input("")
    
count_votes = []
for vote in listofvotes:
    if vote in count_votes:
        continue
    else:
        count_votes.append(vote)
        
    
print("\nVote counts:")
count_votes.sort()
for party in count_votes:
    no_of_votes=listofvotes.count(party)
    print(party, " "*(11-len(party)), "- ", no_of_votes, sep="")