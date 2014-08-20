# A program to count the number of votes for each political party in an election
# Wongwa Giqwa
# 23 April 2014

# Create the display message

def display():
    print('Independent Electoral Commission')
    print('--'*16)

def parties():
    display()
    parties = [] # create an empty list
    party = input('Enter the names of parties (terminated by DONE):\n')
    while party != 'DONE':
        parties.append(party)
        party = input('')
    
        
    print('\nVote counts:')
    counter = {}# use a dictionary
    
    # loop for counting votes  
    for party in parties:
        if not party in counter:
            counter[party] = 1
        else:
            counter[party]+=1
        
    for party in sorted(counter): # sort the parties in the dictionary
        print(party.ljust(10) ,'-',counter[party])
parties()