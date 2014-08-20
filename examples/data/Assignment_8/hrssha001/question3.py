#Shane Horsley
# Program to encode a message
# 6 May 2014
string = input("Enter a message:\n")

def encode(x): #function to encode (only lowercase)
    if x[0].islower(): #only encode lowercase
        if len(x) == 1:
            if x[0]=="z": #special case
                return "a"
            else:
                return chr(ord(x[0])+1)
        elif x[0]=="z": #special case
            return "a" + encode(x[1:])
        
        else:
            return chr(ord(x[0])+1) + encode(x[1:]) #change first letter to one character after it in the alphabet
    else: #any characters that arent lowercase, return the character and the rest of the string
        if len(x) == 1: 
            return x[0]
        else: 
            return x[0] + encode(x[1:])
print("Encrypted message:")
print(encode(string))
