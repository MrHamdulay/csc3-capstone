"""program to encrypt a message using recursion 
   kevin kumasamba
   09 may 2014"""

message=input("Enter a message:\n")

# problem: encrypt a message by moving one letter up
# smaller problem: move one letter up at a time
# if it is a space, leave it alone and move onto the next one

def encrypt(message):
    if message=="":
        return ""
    elif message.isupper():
        return message
    elif not message[0].isalpha():
        return message[0] + encrypt(message[1:])
    elif message[0]=="z":
        return "a" + encrypt(message[1:])
    else:
        return chr(ord(message[0])+1) + encrypt(message[1:])
    
print("Encrypted message:", encrypt(message), sep="\n")
        
    