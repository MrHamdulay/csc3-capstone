"""Program to count the number of pairs of repeated characters in a string
Lorena Dal Maso
10 May 2014"""



#get message from user
message = input("Enter a message:\n")

#create a function to count the number of pairs in the message
def pair (message):
    
    #base case
    if len(message) == 0 or len(message) == 1:
        return 0
    #if a character = the character after it
    elif message[0] == message [1]:
        return 1+pair(message[2:])
    else:
        return pair (message[1:])
pair (message)

#print out the number of pairs in the message for the user to see
print ("Number of pairs: ",pair(message),sep="")
