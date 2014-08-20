#Author: NLXALE001
#Date: 6 May 2014
#Assignment8

#create variables
global message
message = input ("Enter a message:\n")
global indexbegin
indexbegin = 0
global indexcompare
indexcompare = 1
global overlap
overlap = False
global pairs
pairs = 0

def countpairs(indexbegin, indexcompare, message, pairs, overlap):
    if indexcompare == len(message):
        print ("Number of pairs:", pairs)#print final tally
    elif overlap == True: #check that there is no overlap in the pairs
        overlap = False
        countpairs(indexbegin+1, indexcompare+1, message, pairs, overlap)
    elif message[indexbegin] == message[indexcompare]:
        overlap = True
        countpairs(indexbegin+1, indexcompare+1, message, pairs+1, overlap)
    else: #not a pair, call next function
        countpairs(indexbegin+1, indexcompare+1, message, pairs, overlap)


countpairs(indexbegin, indexcompare, message, pairs, overlap)



