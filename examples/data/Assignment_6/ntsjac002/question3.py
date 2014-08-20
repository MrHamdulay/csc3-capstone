'''A program that takes a list of parties from the user and counts the number of votes for each party when it is entered for the second time
Jacob Ntesang
22 April 2014'''

#Ask the user to enter a list of parties and make of each party when it is entered for the 2nd time
print("Independent Electoral Commission")
print("--------------------------------")
The_list = input("Enter the names of parties (terminated by DONE):\n\n")
Parties = []#Empty list of parties
Votes = {}#Empty dictionary for parties and their votes
while The_list != "DONE":
    Parties.append(The_list)
    The_list = input()
    
#Go through the lists of Parties and count the votes
print("Vote counts:")
Str = "{0:<11}-{1:>2}"

for Party in Parties:
    if not Party in Votes:
        Votes[Party] = 1
        
    else:
        Votes[Party] +=1
#print(Votes) sorted alphabetical
for i in sorted(Votes):
    print(Str.format(i,Votes[i]))
    

