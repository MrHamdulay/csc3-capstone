"""count the number of votes in each party
Kamogelo Mphela
20 April 2014"""

print("Independent Electoral Commission")
print("--------------------------------")

#create the list
parties = []
x = input("Enter the names of parties (terminated by DONE):\n")
while x != "DONE":
    parties.append(x)
    x = input("")

#identify the parties
# CREATE A LIST WHERE EACH PARTY APPEARS ONCE!
party = []
for i in parties:
    if i not in party:
        party.append(i)
party.sort()        
#count the number of votes in each party
print()
print("Vote counts:")
x = 0
for i in party:
    count = parties.count(party[x])
    print(i," "*(10-len(i))," - ",count,sep="")
    x +=1