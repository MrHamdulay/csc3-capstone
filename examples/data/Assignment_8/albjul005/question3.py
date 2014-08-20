'''Encrypting message program - Assignment 8
Julian Albert
08-05-2014'''

message = input("Enter a message:\n")

def encrypt(message):
    if len(message) == 1 and message in "abcdefghijklmnopqrstuvwxy": #if 1 character,then encrypt letter
        return chr(ord(message[0]) + 1)
    if len(message) ==1 and message in "z": #if the character is "z", change to "a"
        return "a"
    if len(message) > 1 and message[0] in "abcdefghijklmnopqrstuvwxy": #if <1 character, then run through the function and encrypt each individual character
        return chr(ord(message[0]) + 1) + encrypt(message[1:])
    if len(message) > 1 and message[0] in "z":
        return "a" + encrypt(message[1:])
    else:
        if len(message) == 1:
            return message
        else:
            return message[0] + encrypt(message[1:])
print("Encrypted message:\n"+ encrypt(message))

        
        
        
        
        
        
        