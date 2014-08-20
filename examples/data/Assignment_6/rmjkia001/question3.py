"""Count the votes
Kiara Ramjith
April 2014"""

print("Independent Electoral Commission\n--------------------------------")
parties=[]
names=input("Enter the names of parties (terminated by DONE):\n")
while names != "DONE": #enter names of parties until DONE
    parties.append(names)    #add party name to array
    names=input("")
parties.sort()
votes={} #create an empty dictionary
for name in parties: 
    if name not in votes: #if the current name has not been found in the dictionary, add
        votes[name]=1
    else:
        votes[name]+=1 #running total of votes
print("\nVote counts:")
for name in sorted(votes):
    print("{0:10}".format(name),"-",votes[name])#print a formatted string
    
