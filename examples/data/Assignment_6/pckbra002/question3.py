"""program to count the number of votes for a each political party in an election"""
#Bandon Pickup (PCKBRA002)
#2014/04/21
#Assignment 6 Question 3
print("Independent Electoral Commission")
print("--------------------------------")
party = input("Enter the names of parties (terminated by DONE):\n")
parties=[]#list of all the party votes

while party!= "DONE":
    parties.append(party)
    party = input("")
    
partyList={}#dictionary with each party and their number of votes received
for party in parties:#runs through every item in the list of party votes
    if not party in partyList:#if a party is not included in the dictionary, it is added with a starting value of 0
        partyList[party]=0
    partyList[party]+=1#adds a vote to a particular party's total

keysParty = []
for i in partyList.keys():#creates a list of all the keys in the dictionary so that it can be sorted
    keysParty.append(i)
keysParty.sort()
print()
print("Vote counts:")    
for party in keysParty:#for every party in the keys from the dictionary list
    print(party," "*(10-len(party))," - ",partyList[party],sep="")#prints the name of the party left alligned in a field of width 10 followed by the number of votes they received



