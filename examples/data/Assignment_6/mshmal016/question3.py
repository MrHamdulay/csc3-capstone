''''program to count number of votes
matshepo mashabela
24 april 2014'''
heading="Independent Electoral Commission"
print(heading)
print("-"*32)

#ask for votes
parties=[]
party=input("Enter the names of parties (terminated by DONE):\n")
parties.append(party)
while party!="DONE":
    party=input()
    if party!="DONE":
        parties.append(party)
parties.sort()

#create lists to count and print votes
used= []
votecount= []
for party in parties:
    if party not in used:
        if party!="DONE":
            used.append(party)
            countedvotes=parties.count(party)
            votecount.append(countedvotes)
lengthlist=0
count=0
print()
print("Vote counts:")
for vote in used:
    length=len(vote)
    print(vote," "*(9-length),"-",votecount[count])    
    count+=1



