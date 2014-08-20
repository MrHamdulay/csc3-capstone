#A program that counts the number of votes for each political party in an election
#Author: Emiel Zyde
#Date: 20 April 2014

print("Independent Electoral Commission")
print("--------------------------------")

#prompt user to enter party and create empty list
party = input("Enter the names of parties (terminated by DONE):\n")
party_list = []

#keep adding parties to list while names are being entered
while party != "DONE":
    party_list.append(party)
    party = input("")

#create a list of distinct parties
party_sep = []
for i in party_list:
    if i in party_sep:   #if i is already in the list, continue with the next iteration; otherwise, add it to the list
        continue
    else:
        party_sep.append(i)

party_sep.sort()

print("\nVote counts:")

#count the number of votes for each party and print out the outcome
for i in party_sep:
    votes = party_list.count(i)
    print(i.ljust(10), "-", votes)
    
    