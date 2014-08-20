"""Name: Sibulele Hlongwane
Date: 06 May 2014 
Assignment: Encrypt a message using recursion"""
message=input("Enter a message:\n")

def encrypt(message):
    #Base case: blank message value
    if message=="":
        return ""
    else:
        #if the ordinal value of message character is between 97 and 122. ie: small letter then move character by one and call character again
        if (ord(message[0])==122):
                    s="a"
                    return s+ encrypt(message[1:])        
        if (97<=ord(message[0])<=122):
            s=chr(ord(message[0])+1)
            return s+ encrypt(message[1:])
        #if ordinal value of message=32 i.e: is a space then leave message character as it is, and call function again
        if (ord(message[0])==32):
            return message[0]+ encrypt(message[1:])
        else:
            #if message is not either of the above: i.e: a capital letter then leave message as it is, and recall the function  
            return message[0]+ encrypt(message[1:])
#print the message
print("Encrypted message:\n" +encrypt(message))           