"""program to encrypt string
chris betteridge
06 may 2014"""

#function to return an encrypted string
def encrypt_message(string):
    #testing is all letters are in upper 
    if string.isupper():
        return string 
    if string == "":
        return ""
    #skip spaces when encryting
    if string[0] == " ":
        return " " + encrypt_message(string[1:len(string)])
    #skip fullstops
    if string[0] == ".":
        return "." + encrypt_message(string[1:len(string)])    
    #encrypting
    if string[0] == 'z':
            return 'a' + encrypt_message(string[1:len(string)])     
    else:
        return chr(ord(string[0])+1)  + encrypt_message(string[1:len(string)])

string = input("Enter a message:\n")
print("Encrypted message:\n",encrypt_message(string),sep='')