"""Question 3: Votes
Galya Wolov
23 April 2014"""

#print out the ballot introduction and ask for input of votes
print("Independent Electoral Commission")
print("--------------------------------")
ballot= []
countballot= []
party= input("Enter the names of parties (terminated by DONE):\n")
print()
#add new party to array and separates duplicates
while party != "DONE":
    if party not in ballot: 
        ballot.append(party)
        party= input("")
    else:
        countballot.append(party) 
        party=input("")

#print out ballot with counted parties votes
ballot.sort()
print("Vote counts:")
for item  in ballot:
    x=countballot.count(item)
    print("{:<10}".format(item)+" -", (x+1)) #formats to look the same aligned 10
    



    