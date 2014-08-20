'''counts the number of votes for different parties in a list of votes
tom new
2014/04/12'''
import question1

def count (array):
    '''counts the number of unique items in a list'''
    counter = {}
    for i in array:
        if i in counter:
            counter [i] += 1
        else:
            counter.update ({i: 1})
    return counter

if __name__ == '__main__':
    print ('''Independent Electoral Commission
--------------------------------
Enter the names of parties (terminated by DONE):''')
    votes = question1.getlist ()
    votes.sort ()
    votesfrq = count (votes)
    partylist = list (votesfrq.keys ())
    partylist.sort ()
    print ()
    print ('Vote counts:')
    for i in partylist:
        print (i, ' ' * (11 - len (i)), '- ', votesfrq [i], sep = '')   