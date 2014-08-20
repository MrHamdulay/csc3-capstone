"""Program to count votes in an election
Sithasibanzi Kondleka
23 April 2014"""

print("Independent Electoral Commission")
print("--------------------------------")
parties = {}
party = input("Enter the names of parties (terminated by DONE):\n")

while party != "DONE":
    if parties.get(party,"No Entry")=="No Entry": #setting a default value for if there's no vote for a party
        parties[party]=1
    else:
        parties[party] = parties.get(party)+1 #tallying the votes
    party = input("")

print()
print("Vote counts:")
gap=11 #creating the width
A=(sorted(parties))
for i in A:
    print(i," "*(gap-len(i)),"-"," ",parties.get(i),sep="")