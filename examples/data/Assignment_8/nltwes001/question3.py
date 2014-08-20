#ASSIGNMENT 8
#QUESTION 3
#NLTWES001

message=input("Enter a message:\n")

def encrypt(message):
    if message=="":
        return ""
    else:
        if message[0].islower():
            if message[0]=="z":
                newchar="a"
            else:
                newchar=chr(ord(message[0])+1)
            return newchar + encrypt(message[1:])
        else:
            return message[0] + encrypt(message[1:])
        
print("Encrypted message:")
print(encrypt(message))