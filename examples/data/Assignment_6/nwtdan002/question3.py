"""Compiling a set of votes into a readable format
By Daniel Newton
19/04/14"""

print("Independent Electoral Commission")
print("--------------------------------")
print("Enter the names of parties (terminated by DONE):")

parties=[]      #Shows program the two empty lists to be used
votes=[]
run=True    #Ensures first loop will run

while run:      #Prompts input from user, compiling inputs into a string until the user types DONE.
    party=input()
    
    if party=="DONE":
        break
    parties.append(party)
    
    
while parties != []:    #Evaluates each element in the list 'parties', and adds them to another list until all elements have been evaluated and removed.
    for name in parties:    #Scrolls through the list and counts the number of occurences of an element, adding that number into a new list beside that element, and then removing all occurences of that element for the parties list.
        votes.append("{0:<10}".format(name)+" - "+str(parties.count(name)))
        while name in parties:
            parties.remove(name)   
            
            
votes.sort() #New list sorted alphabetically

print()
print("Vote counts:")

for party in votes: #Each element of new list printed under "Vote counts:"
    print(party)