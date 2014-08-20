'''Program to count the number of votes for each political party in an election
Raeesa Behardien
BHRRAE003
Assignment 6
Question 3'''

print("Independent Electoral Commission")
print("-"*32)

#the input
votes = []

names = input("Enter the names of parties (terminated by DONE):\n")

#create while function
while names != "DONE":
    votes.append(names) #to add another string
    names = input("") #enter more input until done
    
#Count the votes
count_votes={}

for names in votes:
    if not names in count_votes: #if not because checking for truth
        count_votes[names]=0
    count_votes[names] += 1

sort_votes = sorted(count_votes.keys())

#print votes
print("")
print("Vote counts:")
for names in sort_votes:
    print(names + ' '*(10 -len(names)),'-', count_votes[names])
    