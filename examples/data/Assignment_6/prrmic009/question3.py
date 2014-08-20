"""program to count the number of votes for each political party in an election
Mick Perring
25 April 2014"""

print ("Independent Electoral Commission\n--------------------------------")
vote = input("Enter the names of parties (terminated by DONE):\n") # user inputs party names (for each vote)
list_1 = []
list_1.append(vote)       # adds first vote to list_1

while vote != "DONE":     # user (continues to) enter party names until input "DONE" to stop input
    vote = input()
    list_1.append(vote)   # adds votes to list_1

del list_1[-1]  # removes "DONE" from list_1
list_1.sort()   # sorts list_1 alphabetically
print()    
print("Vote counts:")

while len(list_1) > 0:   # counts votes for each party and prints results
    x = list_1[0]
    gap = 11 - len(x)
    c = list_1.count(x)
    print(x, gap*" ", "- ", c, sep="")
    while x in list_1:
        list_1.remove(x)

