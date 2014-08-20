"""08/05/2014
Adam Ruff RFFADA002
Assignment 8 Question 3
Encrypt a string using recursive fuctions"""

message = input("Enter a message:\n")

def encrypt(message):
    if message == "":
        return ""
    elif 97 > ord(message[0]):
        return message[0] + encrypt(message[1:])
    elif message[0] == 'z':
        return 'a'+encrypt(message[1:])
    elif message[0] == ' ':
        return ' '+encrypt(message[1:])
    else:
        return chr(ord(message[0])+1) + encrypt(message[1:])
    
print ("Encrypted message:\n"+encrypt(message))
    