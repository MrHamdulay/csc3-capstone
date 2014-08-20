#AMNTAS003  #Tashfia Amin   #Due Date: 9 May 2014  
#Question 2: Assignment 8   #Count number of pairs of repeated characters

#Ask for input of message
message = input("Enter a message: \n")

#Function to check repeated characters
def rep_char(message):
    if len(message) == 1:                               #If there are fewer than 2 characters, there can be no repetition
            return 0
    elif len(message) == 2:
        if message[0] == message[1]:                    #Check if there is a repeated character
            return 1
        else:
            return 0                                    #If no repetition, do not count anything
    elif message[0] == message[1]:                      #Check to see if there is a repeated pair
        return 1 + rep_char(message[2:])
    else:
        return rep_char(message[1:])
        
print("Number of pairs:", rep_char(message))