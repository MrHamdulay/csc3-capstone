#Author         : Edwin Samuels
#Student number : SMLEDW002
#Date           : 20 April 2014
#Function       : Counts the number of votes
#Title          : Question3


print("Independent Electoral Commission")
parties = input("--------------------------------\nEnter the names of parties (terminated by DONE):\n")
list_parties = []

#Gets parties names from the user till DONE is entered into the programme

while parties != "DONE":
    list_parties.append(parties)
    parties = input("")
print()

list_parties.sort()

current_party =""

print("Vote counts:")

for i in list_parties:

    if i != current_party:
        # Ensures that one party isn't counted twice in a sorted list
        current_party = i
        print("{0:<10}".format(i),"-",list_parties.count(i))
