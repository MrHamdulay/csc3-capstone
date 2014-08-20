"""vote counter
Vahin Gounden
22-04-2014"""

#print heading
print("Independent Electoral Commission")
print("--------------------------------")

#get input
party = input("Enter the names of parties (terminated by DONE):\n")

#make lists
partyvote = []
if party != "DONE":
    partyvote = [party]
    partycount = []

#set up sentiniel and add to list
while party != "DONE":
    party = input()
    if party != "DONE":
        partyvote.append (party)

#sort partyvote
partyvote.sort()

print()
print("Vote counts:")

#count votes
for j in partyvote:
    if j not in partycount:
            #if i == j:
        print("{0: <10}".format(j),"-",partyvote.count (j))
        partycount.append (j)
            
