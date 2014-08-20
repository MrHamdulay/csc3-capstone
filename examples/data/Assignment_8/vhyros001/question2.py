"""Assignment 8 question 2
Find pairs in a string with a recursive function
Ross van der Heyde VHYROS001
7 May 2014"""

def pairs(word):   
    """Returns number of pairs of letters in a word"""
    if word == "" or len(word) ==1: # there can be no pairs if it's 1 char long
        return 0
    elif word[0] == word[1]:
        return 1 + pairs (word[2:])
    else:
        return pairs (word[2:])   
    
mess = input("Enter a message:\n")
p = pairs(mess)
print("Number of pairs:", p)
