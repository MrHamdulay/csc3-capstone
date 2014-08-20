'''a program to count the number of votes for each political party in an election.
fadzai mupfunya
21/04/14'''

#for the title at the top
print("Independent Electoral Commission")
print("--------------------------------")

#for creating a list of parties
parties=[]
parties_list=input("Enter the names of parties (terminated by DONE):\n")
while parties_list != "DONE":
    parties.append(parties_list)
    parties_list = input ("")

#for counting the number of parties in a dicionery
parties2={}
for party in parties:
    if not party in parties2:
        parties2[party]=0
    parties2[party] += 1


#for printing the names of the parties with their votes
print()
print("Vote counts:")

#for sorting parties in order
sorted_parties = sorted(parties2.items(), key=lambda parties2: parties2[0])
for party,vote in sorted_parties:
    aligned =10-len(party)
    print(party," "*aligned+'-',vote)
    

