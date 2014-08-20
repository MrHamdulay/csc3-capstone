""" a program to count the number of votes for each political 
party in an election.
Author: Dominic Manthoko
21 April 201"""

print("Independent Electoral Commission")
print("--------------------------------")

# prompt the user the names of parties
party = input("Enter the names of parties (terminated by DONE): \n")

# create an empty dictionary to store the votes for each party
count = {}

while party != "DONE":
    # if the party name is not already defined in count, add the party add give 
    # it value 1, else just increment the value of a defined party(key)
    count[party] = count.get(party, 0) +1   
    
    party = input("")


print("\nVote counts:")

# print the results for each party on a seperate line
for party in sorted(count):
    print("{0:<10} - {1}".format(party, count[party]))
