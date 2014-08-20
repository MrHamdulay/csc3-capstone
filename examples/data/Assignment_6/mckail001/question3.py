"""Assignment 6 question 3: Program to count number of votes during election
Ailsa Mackay MCKAIL001
2014-04-22"""

print("Independent Electoral Commission") 
print("--------------------------------")
vote = input("Enter the names of parties (terminated by DONE):\n")
votes_list = []
while vote != "DONE":
    votes_list.append(vote) #vote is appended to the votes list if it is not the sentinel
    vote = input("")

parties_list = []

for i in votes_list:
    if i in parties_list: #if a party name has already been encountered in the votes list, it is not added to the party list
                continue
    else:
        parties_list.append(i)

print("")
print("Vote counts:")
for i in sorted(parties_list):
    count = 0
    for j in votes_list: 
        if j == i:
            count += 1
    print(i, (11-len(i))*" ", "-", " ", count, sep="")
    
        