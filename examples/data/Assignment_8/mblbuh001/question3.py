# question3.py
# Name: Buhlebezwe
# Student Number: MBLBUH001
# Date: 07 May 2014

message=input("Enter a message:\n")                                 #get input (message) from the user

def encrypt(message):
    if len(message)<1:
        return ""                                                   #if message is empty then return empty string
    
    elif message[0].islower()==False:
        return message[0]+ encrypt(message[1:])                     #if character is not a lower case, return the character and check the rest of the string
    
    elif message[0]=="z":
        return "a"+ encrypt(message[1:])                            #if character is a "z", then change it to an "a"
    
    else:
        return chr((ord(message[0])+1)) + encrypt(message[1:])      #changes character to next ASCII value and checks characters that follow

print("Encrypted message:\n",encrypt(message),sep="")