#Assignment 9
#Question 2
#Rabia Parker
#Due Date: 09/05/14

#using recursion to count number of repeated pairs of characters in a string

message = input("Enter a message:\n") #get message from user and assigning a variable to that message

def repeated_chars(message): #define function to call it later
    
    if message=="": #message is an empty string
        return 0
    elif len(message)==1: #the message only has one character
        return 0
    
    else:
        if message[0]==message[1]: #first character is the same as second character
            message=message[2:] #message takes new position
            return 1 + repeated_chars(message)
            
        else:
            return repeated_chars(message[1:])
        
print_message=repeated_chars(message)
print("Number of pairs:", str(print_message))
    

    
