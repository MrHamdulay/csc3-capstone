#Phumelele Ndimande
#Assignment 8

def encrypt(secret):

    if secret == "": #stops if secret is empty
        return ""
    else:
        char = secret[0] 
        if char.islower(): #checks for lower case letters
            if char == "z": 
                newchar = chr(ord(char) - 25)
            else: #changes to the next character unicode
                newchar = chr(ord(char) + 1)
            return newchar + encrypt(secret[1:])
        else:
            return char + encrypt(secret[1:])
        
def main():
    secret= input("Enter a message:\n")
    print("Encrypted message:",encrypt(secret),sep="\n")
        
main()
            
