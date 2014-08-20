"""ASSIGNMENT 8 QUESTION 2- FIND THE NUMBER OF PAIRS IN A STRING
EMMA JORDI
8 MAY 2014"""

#get message
message=input("Enter a message:\n")

#define function
def no_pairs(message, n):
    
    #base case
    if n>=len(message)-1: 
        return 0
    
    #recursive step
    else:
        if message[n]==message[n+1]: #if the nth letter is the same as the n+1th
            return 1+ no_pairs(message, n+2) #skip one if it finds a pair
        else:
            return no_pairs(message, n+1) #check subsequent letters

print("Number of pairs:",no_pairs(message, 0))