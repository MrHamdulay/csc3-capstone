"""Akhil Singh
SNGAKH004
23 April 2014"""

print("Independent Electoral Commission\n--------------------------------")
# Get name of parties
party_names=input("Enter the names of parties (terminated by DONE):\n")


#Set variable accumulator
parties=[]
total_parties=[]
#Store names into variable accumulator and only store names that haven't been stored before
while party_names != "DONE":
    parties.append(party_names)
    if party_names not in total_parties:
        total_parties.append(party_names)
    party_names=input("")
        
#Create a new list with votes stored along the side and the party names formated to field width 10
tally_vote=[]
for i in total_parties:
    tally_vote.append("{0:10} - ".format(i)+str(parties.count(i)))
#Sort and output list.
tally_vote=sorted(tally_vote)
print("\nVote counts:")
for a in tally_vote:
    print(a)