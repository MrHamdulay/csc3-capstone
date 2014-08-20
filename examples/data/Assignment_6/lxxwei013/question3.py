"""count number of votes
Michelle Lu
21 April 2014"""

print("Independent Electoral Commission")
print("--------------------------------")

#create a list for parties
parties=[]

#get the votes
names=input("Enter the names of parties (terminated by DONE):\n")
while names!="DONE":
    parties.append(names)
    names=input("")

#iterate to find the different parties
diff_parties=[]
for i in parties:
    if i not in diff_parties:
        diff_parties.append(i)

#sort in alphabetical order
diff_parties.sort()

#count number of votes per party:
partyvotes=[]
for party in diff_parties:
    votes=0
    for vote in parties:
        if party==vote:
            votes+=1
    partyvotes.append(votes)

#format
print("")
print("Vote counts:")
for j in range(len(diff_parties)):
    print("{0:<10}".format(diff_parties[j]), "-", partyvotes[j])