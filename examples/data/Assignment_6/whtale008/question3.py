"""" vote counter
Alexander Whiting
14 april 2014"""

print("Independent Electoral Commission")
print("--------------------------------")
print("Enter the names of parties (terminated by DONE):")

vote = input("")
parties = {}

while vote != "DONE":
    
    if (vote not in parties):
        parties.update({vote:1}) #adding new candiate to dictionary
    else:
        parties[vote] += 1 
    vote = input("")


print()
print("Vote counts:")

for i in sorted(parties): # outputing result with a slight format
    print(i+" "*(10-len(i))+" - "+str(parties[i]))