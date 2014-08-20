"""Assignment 6, question 3:Counts the votes for each party in an election
Dean Gracey
20 April 2014"""

print("Independent Electoral Commission")
print("--------------------------------")

party= input("Enter the names of parties (terminated by DONE):\n")

parties= {}
while (party!="DONE"):

        if(party in parties):
                parties[party] = parties[party]+1
        else:
                parties[party] = 1
        party= input("")
                   
print("\nVote counts:")

for party, votes in sorted(parties.items()):
        print("{0:<10}".format(party)+" - "+str(votes))
