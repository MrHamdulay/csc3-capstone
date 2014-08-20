# Assignment 8-question3
#Annika Brundyn
#encrypt function

def encrypt(message):
    if len(message) == 1:
        if message.islower():
            if message == 'z':
                return 'a'
            else:
                return chr(ord(message) + 1)
        else:
            return message
    else:
        return encrypt(message[0]) + encrypt(message[1:])

string = input("Enter a message:\n")
print("Encrypted message:")
print(encrypt(string))