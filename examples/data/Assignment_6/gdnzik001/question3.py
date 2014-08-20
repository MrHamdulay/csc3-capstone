"""program to count the number of votes for each political party in an election
Zikho Godana
24 April 2014"""

top="Independent Electoral Commission"
print(top)
print("-"*len(top))

parties=[]
parties2=[]

party=input("Enter the names of parties (terminated by DONE):\n")

while party!="DONE":
    parties.append(party)
    party=input("")
print()
print("Vote counts:")
output="{0:<11}- {1:>1d}"
for party in sorted(parties):
    votes=parties.count(party)
    #create another list to ensure that each party is printed once
    if party not in parties2: 
        parties2.append(party)
        print(output.format(party,votes))
    

