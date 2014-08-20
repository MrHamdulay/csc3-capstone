# question2.py
# program to count the number of pairs of letters in a sentence using recursion
# camilla craven
# 9 may 2014

string = input("Enter a message:\n")

def count_adjacent(string):
    
    # if less than two letters, cannot have pairs
    if len(string) < 2:
        return 0
    
    # if string has 2 letters, compare to see if the same
    elif len(string) == 2:
        # if are the same, return 1 (one pair)
        if string[0] == string[1]: 
            return 1 
        # if aren't the same, no pairs - return 0
        else:
            return 0
    
    # if two letters the same, add to the count (and check rest of word)    
    elif string[0] == string[1]: 
        return 1 + count_adjacent(string[2:]) # slice at 2 because don't want triples being counted as 2 pairs
    
    # if two letters not the same, check the second of the two letters with the next letter
    else:
        return count_adjacent(string[1:])# returns value to the previous value of countpairs

print("Number of pairs: "+ str(count_adjacent(string)))