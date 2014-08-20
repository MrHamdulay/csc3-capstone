""" Question 3 / Assignment 8: Message encrypter
Shaheel Kooverjee - KVRSHA004
8 May 2014 """

def encrypt(message):
    if len(message) == 1: #base case
        if message == "z": 
            return "a" #z replaced with a
        elif not message.isalpha() or message != message.lower():
            return message #return same character if not a lower case letter
        else:
            return chr(ord(message)+1) #return next letter if in set [a,y]
    else:
        if message[0] == "z":
            return "a" + encrypt(message[1:]) #z replaced with a plus function repeated with message minus first character
        elif not message[0].isalpha() or message[0] != message[0].lower():
            return message[0] + encrypt(message[1:]) #return same character if not a lower case letter plus function repeated with message minus first character
        else:
            return chr(ord(message[0])+1) + encrypt(message[1:]) #return next letter if in set [a, y] plus function repeated with message minus first character
    
usermessage = input("Enter a message:\n")
print("Encrypted message:")
print(encrypt(usermessage))