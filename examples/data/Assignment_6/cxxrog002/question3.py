""" counting the number of votes
Roger Cox
23/04/2014"""
print("Independent Electoral Commission")
print("--------------------------------")
# empty list
votes=[]

part_name=input("Enter the names of parties (terminated by DONE):\n")

while part_name !="DONE":
        votes.append(part_name)
        part_names=str(part_name)
        part_name=input("")
# fill votes with input
votingparties={}

for vote in votes:
        if not vote in votingparties:
                votingparties[vote]=1
                
        else :
                votingparties[vote]+=1
#create a dictionary
print()
print("Vote counts:")
# sort dictionaries
for votes in sorted(votingparties.keys()):
        print (votes,(" ")*(10-len(votes))," - ",votingparties[votes],sep="")


