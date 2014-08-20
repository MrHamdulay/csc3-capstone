"""Checking for palindromic prime numbers
Christopher Sterley
04/05/2014"""

message=input("Enter a message:\n") #get input for program

def letter_pair_finder(message, number): #function which checks for letter pairs
    if number>=len(message)-1: #stopping point
        return 0
    else:
        if message[number]==message[number+1]: #checks for pairs and skips past this in the string
            return 1 + letter_pair_finder(message,number+2)
        else:
            return letter_pair_finder(message,number+1) #keeps going normally if a pair isn't found
        
print("Number of pairs:",letter_pair_finder(message,0))