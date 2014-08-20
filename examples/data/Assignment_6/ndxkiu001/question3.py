#Kiuran Naidoo
#Assignment 6
#Question 3
#24 April 2014

print("Independent Electoral Commission")
print("--------------------------------")
parties ={}#Define dictionary to store part name and votes


currentParty = input("Enter the names of parties (terminated by DONE):\n")
while currentParty.upper() != "DONE":
    if currentParty not in parties: #Add parties to dictionary if not previously entered
        parties[currentParty] = 1
    elif currentParty in parties:#Update vote count if already in dictionary
        parties[currentParty] = parties[currentParty]+1
    currentParty = input("")#Get next input from user

print()
print("Vote counts:")
for x in sorted(parties): #Sort output
    print ("{0:<10}".format(x),"-",parties[x])#Print output