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


2048 is a puzzle game where the goal is to repeatedly merge adjacent numbers in a grid until the number 2048 is found.  Your task in this question is to complete the code for a 2048 program, using the utility module (util.py) from Question 2 and a supplied main program (2048.py).  The heart of the game is the set of merging functions that merge adjacent equal values and eliminate gaps - you are required ONLY to write these functions in a module (named push.py).

def push_up (grid):
    """merge grid values upwards"""

def push_down (grid):
    """merge grid values downwards"""

def push_left (grid):
    """merge grid values left"""

def push_right (grid):
    """merge grid values right"""          

The original game can be played at: http://gabrielecirulli.github.io/2048/

Note:

    The check_won function from util.py assumes you have won when you reach 32 - this is simply to make testing easier.
    The random number generator has been set to generate the same values each time for testing purposes.

Sample I/O:

+--------------------+
|                    |
|                    |
|          2         |
|2                   |
+--------------------+
Enter a direction:
l
+--------------------+
|                    |
|                    |
|2                   |
|2         2         |
+--------------------+
Enter a direction:
u
+--------------------+
|4         2         |
|                    |
|                    |
|     4              |
+--------------------+
Enter a direction:
d
+--------------------+
|     2              |
|                    |
|                    |
|4    4    2         |
+--------------------+
Enter a direction:
r
+--------------------+
|               2    |
|                    |
|     2              |
|          8    2    |
+--------------------+
Enter a direction:
x

"""
