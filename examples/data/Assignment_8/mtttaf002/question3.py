""" recursive function to encrypt a message
tafara mtutu
06 may 2014"""

def encrypt (string):
    if string == "":
        return ""
    else:
        if 97 <= ord(string[0]) and ord(string[0]) <= 122:
            new = ord(string[0])+1
            if new == 123:
                new = 97
            return chr(new) + encrypt(string[1:])
        else:
            return string[0] + encrypt(string[1:])
        
message = input("Enter a message:\n")
if message:
    print("Encrypted message:", encrypt(message), sep = "\n")