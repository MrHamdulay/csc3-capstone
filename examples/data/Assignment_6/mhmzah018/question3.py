"""Assignment 6 - Question 3
Zaheer Mahmood
23-04-2014"""

print("Independent Electoral Commission")
print("--------------------------------")
#create list to store votes
group_parties=[]
vote_party = input("Enter the names of parties (terminated by DONE):\n")
group_parties.append(vote_party)

#construct loop to accept inputs
while vote_party != "DONE":
    vote_party = input("")
    group_parties.append(vote_party)
    order = group_parties.sort()
group_parties.remove("DONE")
#keep track of number of occurences
new_group = []
print()
print("Vote counts:")
for item in(group_parties):
    if item in new_group:
        continue
    else:
        new_group.append(item)
                
for i in new_group:
    print(i.ljust(10), "-", group_parties.count(i))
            
        
            