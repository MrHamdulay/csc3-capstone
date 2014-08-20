"""Program to Encrypt message
Sithasibanzi Kondleka
9 May 2014"""

message = input("Enter a message:\n")

def encrypt(string):
    char = ord(string[0]) #converting character into its numerical values according to ASCII table
    if string == "":
        return ""
    if len(string) == 1:
        if char >=97 and char < 122:
            return chr(char+1) 
        elif char == 122:
            return "a" 
        else:
            return chr(char) #converting to letter
    if char >=97 and char < 122:
        return chr(char+1) + encrypt(string[1:])
    elif char == 122:
        return "a" +  encrypt(string[1:])
    else:
        return chr(char) + encrypt(string[1:]) #returning the output

print("Encrypted message:\n", encrypt(message), sep="")