'''Program inputs votes and counts total inputted
Nicol Vojacek'''
print("Independent Electoral Commission\n--------------------------------")
votes = []
import collections 
party = input("Enter the names of parties (terminated by DONE):\n")
votes.append(party) #add input to list
while party != "DONE": 
	party = input()
	votes.append(party)
	
for a in votes:
	if a == 'DONE':
		votes.remove(a) #remove last input from list because it is not a vote

votes.sort()

counter = collections.Counter(votes) #count total of repeats of votes in list

print()
print("Vote counts:")
for x,y in sorted(counter.items()): #sort list alphabetically and return output 
	print(x," "*(9-len(x)),"-",y)
	