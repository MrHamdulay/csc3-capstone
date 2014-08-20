# A program that uses a recursive function to encrypt a message by converting all lowercase characters to the next character (with z transformed to a). 
# MUST NOT use any form of loop in the program!


def encrypt(e):
    
    if len(e) == 1:
        if e.islower():
            if e == 'z':
                return 'a'
            
            else:
                return chr(ord(e) + 1)
        
        else:
            return e

    else:
        return encrypt(e[0]) + encrypt(e[1:])

string = input("Enter a message:\n")

print("Encrypted message:")

print(encrypt(string))
