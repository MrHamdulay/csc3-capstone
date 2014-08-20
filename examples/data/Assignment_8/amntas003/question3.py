#AMNTAS003  #Tashfia Amin   Due Date: 9 May 2014
#Question 3: Assignment 8   #Encryption of message using recursion

#Ask for input of message
message=input("Enter a message: \n")

#Function to encrypt message
def encrypt(message):
    if len(message) == 0:
        return ""
    #Check to see if there is a space, do nothing
    elif (ord(message[0])) == 32:                                   
        return " " + encrypt(message[1:])
    #Check to see if there's a fullstop, do nothing
    elif (ord(message[0])) == 46:                                 
        return "." + encrypt(message[1:])
    #Check to see if characters are lowercase letters, encrypt message
    elif 97 <= ord(message[0]) <= 121:                          
        return chr(ord(message[0]) +1) + encrypt(message[1:])
    #Check to see if characters are uppercase letters, do nothing
    elif 65 <= ord(message[0]) <= 90:                           
        return message[0] + encrypt(message[1:])
    #Make "z" loop back to "a"
    elif (ord(message[0])) == 122:                                
        return chr(ord(message[0]) -25) + encrypt(message[1:])

if len(message) ==  0:
    print(encrypt(message),end="")
else:
    print("Encrypted message: \n", encrypt(message), sep="")