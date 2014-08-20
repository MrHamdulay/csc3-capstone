""" Program to printout names of parties and their vote counts
Mazwi Myeza
21 April 2014
Assignment6
Question3
"""
#Creating arrays and printing heading
votes = []
parties = []
partyVotes = []
print("Independent Electoral Commission")
print("--------------------------------")
#Asking user for input and storing it in the created array
vote = input("Enter the names of parties (terminated by DONE):\n")
counter = 0
while vote != 'DONE':
    votes.append(vote)
    counter += 1
    vote = input()
#sorting votes    
votes.sort()  
#populating an array for the parties voted for
for i in range(counter):
    if votes[i] in parties:
        None
    else:
        parties.append(votes[i])
#populating an array for the number of votes a party has recieved
count = 0        
for j in range(len(parties)):
    count = votes.count(parties[j])
    partyVotes.append(count)
print()    
print("Vote counts:")
#printing results in the proper format
for k in range(len(parties)):
    f = "{0:<11}".format(parties[k])
    print(f, partyVotes[k], sep ="- ")