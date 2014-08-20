#Rishen Singh SNGRIS012
#Question Three Assignment 6

print("Independent Electoral Commission\n--------------------------------")

userInput=input("Enter the names of parties (terminated by DONE):\n") #string for all user inputs

userEntry = [ ] #List defined to store userEntries

while (userInput != "DONE"):
    userEntry.append(userInput)  #adds each input into list  
    userInput = input()#takes each user input
party=[]#List to store parties
for k in range (len(userEntry)): #iteration through length of userEntry list
    if(userEntry.index(userEntry[k])==k): #checks list and stores each party name uniquely in party list
        party.append(userEntry[k]) 
party.sort()  #sorts list      
votes=[] #List to store number of votes

for i in party: #iteration through length of party list and sets all votes to 0
    votes.append(0)
for i in range(len(party)):#iteration through length of party list
    for x in range(len(userEntry)):#checks through the userEntry list and counts all occurences(votes) for that party, and increases the vote number for that party
        if(userEntry[x]==party[i]):
            votes[i]+=1
print()         
print("Vote counts:")

for i in range(len(party)):
    print("{0:<11}- {1}".format(party[i],votes[i])) #prints out list of parties and number of votes formatted
    
