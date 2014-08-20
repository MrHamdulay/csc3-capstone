#James Nevin
#Assignment 6, Question 3
#23/04/2014

parties = [] #Going to be two-dimensional list
partyNames = [] #For keeping track of parties
userParty = ""
print ("Independent Electoral Commission\n--------------------------------")
print ("Enter the names of parties (terminated by DONE):")
while (userParty != "DONE"):
    userParty = input()
    if (userParty not in partyNames and userParty != "DONE"): #If party not added yet
        parties.append ([userParty,1]) #Have one vote
        partyNames.append(userParty) #Name now in list
    elif (userParty != "DONE"):
        for x in range (len(parties)): #Finding where party is
            if parties[x][0] == userParty:
                parties[x][1] += 1 #Increasing votes by one

parties = sorted(parties) #Sorting
print ("\nVote counts:")
for x in range (0, len(parties)): #Printing
    print (parties[x][0] + (10-len(parties[x][0])+1)*" " + "- " + str(parties[x][1]))