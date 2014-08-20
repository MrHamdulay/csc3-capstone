'''Program to count the number of votes for each party in an election
21 April 2014
Matshepo'''

#Declare lists for the party names and the votes of the parties respectively
allvotes = [] #keeps track of the names of parties as they are inputted
parties = [] #augmented list of the parts
votes = [] #the number of votes each party in the parties has

#Receive the party names froom the user
print("Independent Electoral Commission \n--------------------------------")
partyname = input("Enter the names of parties (terminated by DONE): \n")

while not partyname.upper() == 'DONE':
    #place the party name in the voting record
    allvotes.append(partyname)
    
    #add the name to parties if it is not in the list already
    if not partyname in parties:
        parties.append(partyname)
 
    partyname = input('')
print()
    
parties.sort()
for i in parties:
    #determine the number of votes each party has and place it in a list
    number_of_votes = allvotes.count(i)
    votes.append(number_of_votes)
    
print('Vote counts:')
for i in range(len(parties)):
    string = '{0:<10} - '  + str(votes[i])
    print(string.format(parties[i]))