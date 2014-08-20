# Assignment 8: Question 2 
# Gadziraiushe Bangure: BNGGAD001
# May 9, 2014

# ----------------------------------------------------------------------
# A program that uses a recursive function to count the number of pairs of repeated characters in a string.  Pairs of characters cannot overlap.  You MUST NOT use any form of loop in your program!
# ----------------------------------------------------------------------



s = input('Enter a message:\n')


def pairing(s):
    
    if len(s)==0 or len(s)==1:  # Base condition
        return 0
    
    elif s[0]==s[1]:
        return 1 + pairing(s[2:])  # count the number of pairs
    
    elif s[0]!=s[1]:# index 0 is eliminated, move to the next character
        return pairing(s[1:])# from index 1 to the end of s

print('Number of pairs:',pairing(s))
    