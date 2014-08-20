#Jason Smythe
#CSC 1015
#SMYJAS002
#assignment 6
#question 3
votes = []
uniqueParties = set()
progComment = "Independent Electoral Commission\n--------------------------------\nEnter the names of parties (terminated by DONE):\n"

vote = input(progComment)
while vote != "DONE":
	votes.append(vote)
	uniqueParties.add(vote)
	vote = input()
print()

uniquePartiesList = list(uniqueParties)
#print(uniquePartiesList)
uniquePartiesList.sort()
#print(uniquePartiesList)
print("Vote counts:")
for party in uniquePartiesList:
	spaceLength = 10 - len(party)
	string = party + (" "*spaceLength) + " -"
	partyCount = votes.count(party)
	print(string, partyCount)
		 
	 




"""
Independent Electoral Commission
--------------------------------
Enter the names of parties (terminated by DONE):
apples
oranges
oranges
oranges
pears
bananas
bananas
kiwis
oranges
apples
oranges
DONE

Vote counts:
apples     - 2
bananas    - 2
kiwis      - 1
oranges    - 5
pears      - 1
"""
