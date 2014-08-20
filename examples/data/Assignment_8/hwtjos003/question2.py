"""letter pair count
Joshua Hewitson
2/5/2014"""

pairs = 0

def check_pair(input1):
    # input1 is shortened each time and if it is of length 1 or 0 there will be no more pairs
    if len(input1) <= 1:
        return
    
    # if there is a pair at the start:
    if input1[0] == input1[1]:
        # the first two letters, forming the pair, are removed and 'pairs' is incrimented
        global pairs
        pairs += 1
        input1 = input1[2:len(input1)]
        # check_pairs is now run again with a shortened input
        check_pair(input1)
    else:
        #otherwise input1 is only sortened by one character and chaeck_pairs is run again
        input1 = input1[1:len(input1)]
        check_pair(input1)

string1 = input("Enter a message:\n")
check_pair(string1)
print ("Number of pairs:" , pairs)