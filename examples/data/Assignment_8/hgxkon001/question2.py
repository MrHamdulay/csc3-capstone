#Konrad Hugo
#Assignment 8 question 2
# 2014-05-08

message = input("Enter a message: \n")
count = 0

def pair_counter(message,count): #function counting number of pairs of letters in a string
    
    if len(message) == 0 or len(message)==1: #the condition that,when met, will break the recursion
        print("Number of pairs:",count)
    
    elif message[0] == message[1]:
        #this is the core of the pair counter:if two adjacent letters =, the
        count += 1

            
        
        #pair counter
        return pair_counter(message[2:],count) #acts as loop, feeding the function new message and count values, keeping it up to date
    
    else:
        return pair_counter(message[1:],count) #Alternative action, if no pair found in the first two letters, carries on with recursion
pair_counter(message,count) #initiation station
    