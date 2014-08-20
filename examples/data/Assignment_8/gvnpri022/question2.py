"""Question 2- Assignment 8- checking for pairs in a string using recursion
GVNPRI022- Prinesan Govender
09 May 2014"""
msg= input("Enter a message:\n")


def check_pairs(msg):
    if len(msg)<=1: #base case -no pairs
        return 0
    
    else:
        if msg[0]==msg[1]: #if found one pair
            return check_pairs(msg[2:])+ 1 #add that pai and check rest of the string
        
        else:
            return check_pairs(msg[1:]) #check rest of the string


print("Number of pairs:",check_pairs(msg)) #output