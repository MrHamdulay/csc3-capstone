"""Recursive function to encrypt messages
Joseph Preyer
6 May 2014"""

msg=input("Enter a message:\n")
print("Encrypted message:")

def encrypt(msg):
    
    #Base case: do not operate on msg if it is an empty string
    if len(msg)>0:
        #If the character is a space, print a space (ie. do not encrypt) and call next character
        if msg[0]==" ":
            print (" ", end="")
            encrypt(msg[1:])
        #print the character represented by the ord of the original character +1, then call next character
        elif msg[0]=="z":
            print ("a",end="")
            encrypt(msg[1:])
        elif msg[0]==".":
            print(".",end="")
            encrypt(msg[1:])
        elif msg[0].isupper():
            print (msg[0],end="")
            encrypt(msg[1:])
        else:
            print (chr(ord(msg[0])+1),end="")
            encrypt(msg[1:])
encrypt(msg)