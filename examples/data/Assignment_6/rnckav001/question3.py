#CSC ass.6 Q3 voting
#Kavir Ranchod rnckav001
#24/04/2014

#intialise dictionary
numvotes={}
#fetch first party name
party=input("Independent Electoral Commission\n--------------------------------\nEnter the names of parties (terminated by DONE):\n")
while party!="DONE":
    #check if party's first vote, if not, add to key for the value "party", else, get new party
    if party in numvotes.keys():
        numvotes[party]+=1
    else:
        numvotes[party]=1
    party=input('')
print()
print("Vote counts:")
#print out vote numbers in columns
for key in sorted(list(numvotes.keys())):
    print(key.ljust(10),"-",numvotes[key])