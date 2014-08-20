# Aaron Krishna
# 24 April 2014
# A program that prints out the names of the parties and their vote counts, with the parties listed in sorted order

party = {} #empty dictionary
print("Independent Electoral Commission") #print that stuff
print("--------------------------------")
name = input("Enter the names of parties (terminated by DONE):\n") #requests name of party

while name != "DONE": #adds to dictionary and counts keys
    if name in party:
        party[name] += 1 
    else:
        party[name] = 1
    name = input()

sort_party = sorted(party.keys()) #sorts
print()
print("Vote counts:")

for name in sort_party:
    print("{:<10}".format(name), " - ", party[name], sep ="") #prints the formatted answer