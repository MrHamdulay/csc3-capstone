"""Count the number of votes for political parties
Jason Findlay
24/04/2014"""


print("Independent Electoral Commission")
print("--------------------------------")

votes=[]
party_temp=""
party=input("Enter the names of parties (terminated by DONE):\n\n")

#Populate list
while party!="DONE":
    votes.append(party)
    party=input()
votes.sort()
print("Vote counts:")
for party in votes:
    if party!=party_temp:
        party_temp=party
        #print the name of the party in a field of length 10 and fill
        #the field with spaces. Then print a count of the number of the
        #specific party name in the list of votes
        print(party,(10-len(party))*" "," - ",votes.count(party),sep="")
