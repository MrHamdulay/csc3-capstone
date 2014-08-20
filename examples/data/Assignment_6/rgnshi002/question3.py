#Program to count votes for an election
#Shivam Ragoonaden

Parties = {}
print("Independent Electoral Commission")
print("--------------------------------")
name = input("Enter the names of parties (terminated by DONE):\n")


while name != "DONE":  #Sentinel
    if name in Parties: #Check if name is in parties
        Parties[name] = Parties[name] + 1    #Add vote to party
    else:
        Parties[name] = 1 #Initialise Party with the one vote given already
    name = input("")
    
            
print()
print("Vote counts:")

for key, value in sorted(Parties.items()): #Loop through the alphabeticallt sorted dictionary to get the party and number of votes
    spaces = 11 - len(key) #Determine number of spaces
    print(key + spaces*" " + "- " + str(value))