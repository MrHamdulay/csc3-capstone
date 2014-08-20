"""polling system a vote of parties
tafara mtutu
20 april 2014"""

party = []
votes = {}

print("Independent Electoral Commission\n--------------------------------")

entry = input("Enter the names of parties (terminated by DONE):\n")
while entry == "":
        entry = input()
        
while entry.lower() != "done":
        party.append(entry)
        entry = input()
        while entry == "":
                entry = input()
        
for i in party:
        if i in votes:
                continue
        else:
                votes[i] = party.count(i)
entry = []      
print("\nVote counts:") 
for i in votes:
        temp = i+ " "*(11-len(i))+"- "+ str(votes[i])
        entry.append(temp)
entry.sort()
for i in entry:
        print(i)


        
