"""Mphuthi Mamorena
Question 2
Assignment 8
CSC1015F
08 May 2014"""

message=input("Enter a message:\n")
def pairs(message):
    if len(message)<=1: # creating a base case
        return 0
    
    if message[0]==message[1]:# comparing the two strings next to each other
        return 1 + pairs(message[2:])# recursive step
    else:
        return pairs(message[1:])# recursiive step again
print("Number of pairs:",pairs(message))# calling the function n printing the number of pairs
    
    
