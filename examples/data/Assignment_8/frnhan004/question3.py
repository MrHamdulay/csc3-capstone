"""Question 3 - Assignment 8
FRNHAN004
5 May 2014"""
msg=input("Enter a message:\n")
def encrypt(msg):
        if msg=="": #base case-if there is nothing left in the string
                return ""
        else:
            if msg[0].isupper(): #if the character is in uppercase, leave it and encrpyt rest of message 
                chr(ord(msg[0]) + 98)
                return msg[0] + encrypt(msg[1:])
            else: #if character is in lower case, encrypt it and the rest of the message
                if msg[0].isalpha(): #if character is alphabetical, encrypt
                        x=msg[0]
                        if x=='z': #if the character is 'z' change to a and encrypt rest
                                return 'a' + encrypt(msg[1:])
                        return (chr(ord(x) + 1)) + encrypt(msg[1:])                        
                        
                else: #if character is numerical, leave it and encrypt rest of message
                        return msg[0] + encrypt(msg[1:])
                        

    
print("Encrypted message:\n", encrypt(msg), sep="")
