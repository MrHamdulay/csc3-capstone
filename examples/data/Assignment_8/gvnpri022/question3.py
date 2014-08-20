"""Question 3- Assignment 8- encryption using recursion
GVNPRI022- Prinesan Govender
09 May 2014"""
msg= input("Enter a message:\n")

def encrypt(msg):
    if len(msg)==0: #baseCase - return messgae
        
        return msg
    
    else:
        if (not (msg[0].isalpha())): #checking if alphabet
            return msg[0] + encrypt(msg[1:])
        
        elif (msg[0].isupper()): #check if upper case
            
            return msg[0] + encrypt(msg[1:])
        
        
        
        elif(msg[0]=='z'): #if z move it to a
            return 'a'+ encrypt(msg[1:])
        
        
        
        else: #move to next unicode value and convert to character
            return chr(ord(msg[0])+1) + encrypt(msg[1:])
        
print("Encrypted message:")
print(encrypt(msg))