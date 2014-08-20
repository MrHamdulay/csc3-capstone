"""program to encrypt
nasonkwe hampwaye
2014-05-08"""

message=input("Enter a message:\n")
def encrypt(message):
    #base case
    if message=='':
        return message
    #recursion step    
    else:
        if message[0]=="z":
            return "a"+encrypt(message[1:])
        elif message[0]==message[0].upper():
            return message[0]+encrypt(message[1:])

        elif message[0]==" ":
            return message[0]+encrypt(message[1:])
        elif message[0]==message[0].lower():
            return chr(ord(message[0])+1)+encrypt(message[1:])
            
print("Encrypted message:")
print(encrypt(message))                                                  
                    