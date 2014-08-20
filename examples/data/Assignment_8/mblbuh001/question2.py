# question2.py
# Name: Buhlebezwe
# Student Number: MBLBUH001
# Date: 07 May 2014

message = input("Enter a message:\n")                   #get input (message) from user

def count_pairs(message):
    if len(message)<2:
        return 0                                        #if message has less than 2 characters, then it has 0 pairs, thus return 0
    else:
        if message[0]==message[1]:
            return 1 + count_pairs(message[2:])         #checks if adjacent characters are the same, if they are return 1 pair and check the next two adjacent characters
        else:
            return count_pairs(message[1:])             #slices message to check if next two adjacent characters are the same
        
print("Number of pairs:",count_pairs(message))          #prints number of pairs of characters in message