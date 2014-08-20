#Assignment 6.3
#Michael Gant
#20/04/2014

#Voting counter
import collections

sText = ""
dVotes = {}

print("Independent Electoral Commission")
print("--------------------------------")
sText = input("Enter the names of parties (terminated by DONE):\n")

while sText != "DONE": #Receives input, checks if the candidate is already in the dictionery and either adds to the running total or creates an entry for the candididate
        if sText in dVotes.keys():
                dVotes[sText] = dVotes[sText] + 1 
        else:
                dVotes.update({sText : 1})
        sText = input("")
        
print()
print("Vote counts:")
orderedVotes = collections.OrderedDict(sorted(dVotes.items())) #sorts dictionery by key
for k in orderedVotes: #runs through the dictionery and outputs the keys and values
        print(k + " "*(10-len(k)) + " - " + str(orderedVotes[k]))
        
        