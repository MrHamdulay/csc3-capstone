#election fun times
#julia breakey
#21 april 2014

#input votes
print("Independent Electoral Commission")
print("--------------------------------")
votes={}
vote=input("Enter the names of parties (terminated by DONE): \n")
while vote!="DONE":
    if vote in votes:
        votes[vote]+=1
    else: votes[vote]=1
    vote=input("")
    
#print votes
print("")
print("Vote counts:")
for key in sorted(votes): #alphabetical order
    print(key, " "*(11-len(key)), "- ", votes[key], sep="")