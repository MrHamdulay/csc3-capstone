""" A program that uses a recursive function to encrypt a message by converting all lowercase characters to the next character
Author: Emiel Zyde
Date: 3 May 2014 """ 

def encrypted_message(message):
    if message == "":        #base case/ termination 
        return message
    elif message[0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":   #ensures that uppercase letters are dealt with effectively
        return message[0] + encrypted_message(message[1:])
    elif not message[0].isalpha():   #deals with spaces and punctuation marks, as well as other non-alphabetical characters 
        return message[0] + encrypted_message(message[1:])
    elif message[0] == "z":                 #ensures z is converted to a
        return "a" + encrypted_message(message[1:])
    else:
        return chr(ord(message[0])+1) + encrypted_message(message[1:])

#get input from user and print out the encrypted message 
message = input("Enter a message:\n")
print("Encrypted message:")
print(encrypted_message(message))