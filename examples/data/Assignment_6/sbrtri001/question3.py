''' Assignment 6, question 3
Count votes for political parties
Tristan Subroyen
22 April 2014 '''

def voteCounter():
    ''' inputs names of party to vote for; counts votes for each party input and displays '''
    
    # initializations
    parties = {} 
    party = ''
    
    # Print menu
    print("Independent Electoral Commission")
    print("--------------------------------")
    print("Enter the names of parties (terminated by DONE):")
    
    while party != 'DONE': # loop is terminated by 'DONE'
        party = input() # input the party name
        if party in parties: # if the party has already been entered into the dictionary, add a vote
            parties[party] += 1
        else:
            parties[party] = 1 # if the party does not yet exist, create its entry along with one vote
            
    del parties['DONE'] # deletes that pesky 'DONE' from the dictionary. Don't want that naughty guy causing mischief in our dictionary now, do we?
    print('')
    print("Vote counts:")
    # print the dictionary in required format
    for i in sorted(parties):
        length = 10-len(i) # calculates spaces needed for width
        print(i + " "*length + " - " + str(parties[i])) # displays party name, required amount of spaces for format and the number of votes
        
        
# INVOKE!
if __name__ == '__main__':
    voteCounter()