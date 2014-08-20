# Aaron Krishna
# 7 May 2014
# A program that encrypts a message by converting all lowercase characters to the next character

def encrypt(message): #function that encrypts a message
    encrypted_message = ""
    if len(message) < 2:
        if message[0].isalpha():
            if message[0] == "z":
                return "a"
            else:
                return chr(ord(message[0]) + 1)
        if message[0].isupper():
            return message
        if message[0] == " ":
            return message
        else:
            return message
    elif message[0].isupper(): 
        return message[0] + encrypt(message[1:])
    elif message[0] == " ":
        return message[0] + encrypt(message[1:])    
    elif message[0].isalpha():    
        if message[0] == "z":
            encrypted_message += "a"
            return encrypted_message + encrypt(message[1:])
        else:
            encrypted_message += chr(ord(message[0]) + 1)
            return encrypted_message + encrypt(message[1:])
    else:
        return message[0] + encrypt(message[1:])    
    
   
message = input("Enter a message:\n")

print("Encrypted message:\n" + encrypt(message))