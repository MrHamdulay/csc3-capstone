""" Program to count number of votes
Aubrey Baloi
23 April 2014"""


print("Independent Electoral Commission")
print("--------------------------------")

def sort(names):
    amu = []
    for i in names:
        if i not in amu:
            amu.append(i)
    amu.sort()
    return amu

def words():
    words = [] # Get an input of words
    word = input('Enter the names of parties (terminated by DONE):\n')
    
    counter = {}
    
    while word != 'DONE':
        words.append(word)
        word=input()
        
    for word in words:  
        if not word in counter:
            counter[word] = 1
        else:
            counter[word] += 1
            
    print('\nVote counts:')
    sortd = sort(words)           
        # print out counters
    for word in sortd:
        a = 9
        b = len(word)
        c = a - b
        print (word,' '*c,'-', counter[word])
        
        
words()