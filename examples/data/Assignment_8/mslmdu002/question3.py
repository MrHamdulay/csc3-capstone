"""This program uses a recursive function to encrypt a message by converting
alllowercase characters to the next character (with z transformed to a)
Masilela Mduduzi
7 may 2014"""
string = input("Enter a message:\n")
def encrypt(string):
    if len(string) == 0:
        return ""
    #check if the string is alpha or lower cases
    elif string[0].isalpha() and string[0].islower():
        
            return chr(97+(ord(string[0])+1-97)%26) + encrypt(string[1:])
    else:
        
        return string[0] + encrypt(string[1:])

print("Encrypted message:\n"+encrypt(string))

        
    
