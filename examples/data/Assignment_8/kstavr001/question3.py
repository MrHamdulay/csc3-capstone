#Assignment 8, Question 3
#Avreyna Kistensamy
#3 May 2014

def encode(message):
    if len(message) < 1:
        return ""
    else:
        if message[0].islower():
            bf = ord(message[0])
            if bf < ord('z'):
                af = chr(bf+1)
            else:
                af = "a"
            encrypted = af
        else:
            encrypted = message[0]
        return encrypted + encode(message[1:])
    
    
x = input("Enter a message:\n")
message = x
print("Encrypted message:\n",encode(message), sep="")