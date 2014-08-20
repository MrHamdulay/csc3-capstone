"""program to encrypt a message
Kristin Kinmont
3 May 2014"""

def encrypt(message):
    if message == "":
        return ""
    #if ord(message[0])<97 or ord(message[0]) >122:
        #return message[0]+ encrypt(message[1:])
    elif message[0] == " " or ord(message[0])<97 or ord(message[0]) >122:
        return message[0]+ encrypt(message[1:])
    elif message[0] == "z":
        return chr(ord(message[0]) - 25) + encrypt(message[1:])
    else:
        return chr(ord(message[0]) + 1) + encrypt(message[1:])

message = input("Enter a message:\n")
print("Encrypted message:")
print(encrypt(message))