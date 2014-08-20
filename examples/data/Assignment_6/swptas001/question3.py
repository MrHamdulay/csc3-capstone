### Tashiv Sewpersad (SWPTAS001)
### Assignment 6 - Question 3
### 2014 - 04 - 20

## Live Code
# the heading
sHeading = "Independent Electoral Commission" + "\n" + "-"*32
print(sHeading)
# get input
aParties = {}
sParty = input("Enter the names of parties (terminated by DONE):\n")
while sParty.upper() != "DONE":
	if sParty in aParties:
		aParties[sParty] = aParties[sParty] + 1
	else:
		aParties[sParty] = 1
	sParty = input("")	
# generate output
Output = "{0:<10} - {1}"
print("\nVote counts:")
SortedParties = []
for Party in aParties:
	SortedParties.append(Party) #Generates a sorted list of parties
SortedParties.sort() # default sorted order	
for SortedParty in SortedParties:
	print(Output.format(SortedParty,aParties[SortedParty]))
	# Prints in default sorted order