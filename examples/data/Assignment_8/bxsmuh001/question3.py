#Assignment 8, Question 3
#Author: Muhammad Sabir Buxsoo (BXSMUH001)
#Class: CSC1015F 2014
#Date Created: 08/05/2014

#This program is designed to encrpyt a message.
#Pre-condition: Input string.
#Post-condition: Output encrypted message

#Creating a function to encrypt the message.
#Pre-condition: Take  message, check message(if null, 1 letter), then check for lower case and encrypt.
#Post-condition: return encrypted message.
def caesarCipher(message):
    if len(message) == 0:
        return "" #No message
    else:
        encryptedMsg = ""
        if ((message[0]) == "z"): encryptedMsg = "a" #If character is z replace with a.
        elif ((message[0]) == " "): encryptedMsg = " " #If character is blank spaced, nothing changes.
        elif (message[0].islower()): encryptedMsg = chr(1+ord(message[0])) #Check for lowercase letter and encrypts, by changing the character to the next.
        else: encryptedMsg = message[0] #Upper case letter is not encrypted.
            
        return encryptedMsg + caesarCipher(message[1:])

#Checking if this file is being run as a standalone.
if __name__ == '__main__':    
    userInput = input("Enter a message:\n")  
    print("Encrypted message:")
    print (caesarCipher(userInput))