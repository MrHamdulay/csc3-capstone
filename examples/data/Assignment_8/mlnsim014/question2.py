'''Program to calculate number of pairs in a word
Simangaliso Mlangeni
MLNSIM014
07 May 2014
Assignment 8, question 2'''

def pairsCount(s):
    '''function that counts number of pairs'''
    if len(s)==1:#base case that checks when the length of the word is 1 and avoids indexing out of range
        return 0
    elif len(s)<=3:
        if s[0]==s[1]:
            return 1 
        else:
            return 0 + pairsCount(s[1:])
    elif s[0]==s[1]:#checks if character is equal to next chararcter in the string
        return 1 + pairsCount(s[2:])#adds 1 to the count if character has a pair and recurses
    else:
        return 0 + pairsCount(s[1:])
    
s = input("Enter a message:\n")#variable that stores string
print("Number of pairs:", pairsCount(s))#Prints number of pairs in a string