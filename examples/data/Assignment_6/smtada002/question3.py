'''Assignment 6 question 3 Political party voting
Adam Smith
23 April 2014'''

print("Independent Electoral Commission")
print("--------------------------------")

partyVotes = {} #creates dictionary to store names of parties and number of votes
partyVotes = {input("Enter the names of parties (terminated by DONE):\n"): 1}

while "DONE" not in partyVotes: 
    UserInput = input()
    if UserInput == "DONE": #breaks the loop if the user inputs DONE
        break
    
    elif UserInput in partyVotes: #if the party exists increments votes
        partyVotes[UserInput] += 1
        
    else: # if it doesn't creates party
        partyVotes[UserInput] = 1

print()
print("Vote counts:")
for partyName in sorted(partyVotes): #sorts and formats parties befor output
    if partyName!= "DONE":
        formattedName = ('{0:<11}').format(partyName) 
        print(formattedName + "- " + str(partyVotes[partyName]))
    