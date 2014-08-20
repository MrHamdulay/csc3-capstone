# Program for printing the number of votes for each party
# Lwazi Shezi
# 25 April 2014


print('Independent Electoral Commission\n--------------------------------')
print('Enter the names of parties (terminated by DONE):')

# Initialise all variables to be used
party_votes = []
next_party = ''

# get the votes for each party
while next_party != 'DONE': 
    next_party = input()  
    if next_party != 'DONE':
        party_votes.append(next_party)
    
    

# print out the number of votes for each party in alphabetical order
parties_sorted = sorted(party_votes) # sort the parties

# initialise all variables to be used in iterations
vote_count_list = []   # list to keep the number of votes for each party
parties = []           # list to keep the names of all parties in alphabetical order

print('\nVote counts:')  

for i in range(0,len(parties_sorted)):
    vote_count = 0
    for j in party_votes: # count the number of votes for each party
        if parties_sorted[i] == j:
            vote_count += 1
        else: continue
    if parties_sorted[i] != parties_sorted[i-1]: # update the vote count list and the party name list only if the party has not been encountered before
        vote_count_list.append(vote_count)
        parties.append(parties_sorted[i])
        
# The program would have complications if there is only one party voted for. This is to account for that problem
if parties == [] :
    if party_votes != [] :
        parties.append(party_votes[0])
        vote_count_list.append(str(len(party_votes)))
counter = 0

# finally print the party names and their corresponding vote numbers
for i in parties:
    print('{0:<10}'.format(i)+' - '+str(vote_count_list[counter]))
    counter += 1
    