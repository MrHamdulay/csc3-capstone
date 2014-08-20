"""Shriya Roy
8 May 2014
program that encrypts message"""
def encrypt(n,z):#2 parameters for the message
    if n=="":# if this reaches the end of the string, return the encrypted message
        return print("Encrypted message: \n"+z)
    else: 
        x=n[0]
        x=ord(n[0])
        if 122>x>=97: #checking if the ordinal is between a and z
            y=x+1
            z=z+chr(y)
            return encrypt(n[1:],z)
        elif x==122:
            z+="a"
            return encrypt(n[1:],z)
        else:
            
            z+=chr(x)# if the ordinal does not lie between 97 and 122, it returns the same position as before
            return encrypt(n[1:],z)
        
       
n=input("Enter a message: \n")      
encrypt(n,"")
        
        
