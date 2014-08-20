"""Keyoolin Padayachee
Voting program
24 April 2014"""

print("Independent Electoral Commission\n--------------------------------\nEnter the names of parties (terminated by DONE):") 

done = ""
parties = [] #creates an array of parties
votes = [] #creates an array of votes
while done != "DONE":
    string = input()
    if string == "DONE":
        break
    if string not in parties:
        parties.append(string) # appends to the parties list if not already in list
    votes.append(string) # appends the votes
    
parties.sort()
print()
print("Vote counts:")
for i in range(len(parties)):
    print("{0:<10}".format(parties[i]),votes.count(parties[i]),sep = " - ")