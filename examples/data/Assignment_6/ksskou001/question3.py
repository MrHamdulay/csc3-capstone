'''This program count and displays the vote of each political party in an election
Kouame Hermann KOUASSI
19 april 2014'''

def get_list():
    '''get the list of all the votes'''
    all_votes = []
    #print the prompt statement to avoid repetition in the loop
    print('Enter the names of parties (terminated by DONE):')
    #iterate indefinitely
    while True:
        vote = input('')
        #break loop when input enter is 'DONE'
        if vote == 'DONE':
            break
        #store all the votes into the array all_votes
        all_votes.append(vote)
    return all_votes
        
def counter(list):
    '''count the vote of each party and match to the party name'''
    #create a list to store parties which vote counts are done
    counted_party = []
    #create a dictionary to match party up with its vote
    party_and_count = {}
    #iterate over all the votes
    for i in list:
        #execute only if count of party not yet done
        if i not in counted_party:
            #count the number time each party appears in the list of all the votes
            party_count = list.count(i)
            #match up the vote count of each party with its name
            party_and_count[i] = party_count
            #add the party to the string of parties which counts are done
            counted_party.append(i)
    #return the matching dictionary
    return party_and_count

def display(dictionary):
    '''prints the parties and their vote counts in an alphabetical order'''
    parties = sorted(dictionary)
    #assume that the longest party name makes 10 characters
    for i in parties:
        print(i,' '*(10-len(i)), ' - ', dictionary[i],sep = '')
        
def main():
    '''main function'''
    #print the welcoming message
    print('Independent Electoral Commission')
    print('--------------------------------')
    #get list of all the votes
    votes = get_list()
    #count and match up each count with party name
    dictionary = counter(votes)
    #display party names follow by their vote counts
    print('\nVote counts:')
    display(dictionary)
 
if __name__=="__main__":
    main()
        