#Assignment 6, Question 3
#Author: Muhammad Sabir Buxsoo (BXSMUH001)
#Class: CSC1015F 2014
#Date Created: 21/04/2014

#This program is designed to count the number of votes for each party given a list of parties.
#Pre-condition: Input list of parties to be elected followed by sentinel "DONE".
#Post-condition: Output  number of votes for each party.

#Header.
print("Independent Electoral Commission")
print("--------------------------------")
print("Enter the names of parties (terminated by DONE):")

#Initial Values.
partyVotes = [] #The list that will contain the votes for all parties.
countedVotes = {} #A dictionary which will assign each party to it's number of votes.
enterParty = "" #Initializing input.

#As long as sentinel value "DONE" is not reached, keep taking input from user.
while(enterParty != "DONE"):
    enterParty = input("")
    if(enterParty == "DONE"): #Break out of loop when sentinel value is reached.
            break    
    partyVotes.append(enterParty) #Append vote to partyVotes list.

#Creating maximum width length. Making sure program can cater for any name length.
#.#Pre-condition: Go through list of partyVotes and check the length of each element with widthLength. 
#.#Post-condition: Assign maximum value to width to widthLength.
widthLength = 10 #Initialize value of widthLength. 10 is the minimum width.

#Check widthLength with length of each partyVote elements. Update widthLength if necessary.
for i in range(len(partyVotes)):
    if(len(partyVotes[i]) > widthLength):
        widthLength = len(partyVotes[i]) #New value of width length (if widthLength > 10).


print("\nVote counts:") #Prints anther heading.

#Creating the dictionary with each party and the number of votes it received.
#.#Pre-condition: Take first element of partyVotes list and check for any duplicates. Update the counter(countParty) accordingly.
#.#Post-condition: Take the party and it's counted value and add it to the dictionary. Then delete that party from the list since it is now redundant to the list. Repeat the process for all parties left, till the list is emptied.
while(partyVotes != []):
    countParty = 0  #Initializing value of count.
    for i in range(len(partyVotes)):
            if(partyVotes[i] == partyVotes[0]): #Checking each element with the first element, where element = party
                countParty = countParty + 1 #If similar party(element) is found, update counter.
    
    countedVotes[partyVotes[0]] = countParty #Add the party and it's total number of votes as a key:value pair to the dictionary(countedVotes).
    
    #Deleting the party whose votes have been counted from the list, to avoid redundancy.
    #.#Pre-condition: Start from the last element and check if element is equal to the first element. 
    #.#Post-condition: As long as condition is satisfied, delete the element from the list and finally delete the first element of the list(when j==0).
    for j in range(len(partyVotes)-1, -1, -1):
        if(partyVotes[j] == partyVotes[0]):
            del partyVotes[j]
            
#print(countedVotes)

#Sort each party alphabetically from the dictionary and use format to print party and it's number of votes.
for key,value in sorted(countedVotes.items()):
    print(('{:<'+ str(widthLength) +'}').format(key), " - ", value, sep="")