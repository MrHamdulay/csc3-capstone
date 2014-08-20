#Assignment 8
#Question 3
#Barry Su
#8 May 2014
#Program using recursion to encrypt messages

#get string to encrypt
string=input("Enter a message: \n")

def encrypt(string):
    if len(string) == 1:        #check if string is one charac
        if string.islower():    #check if string is lowercase
            if string == "z":   #check if string is letter "z", if it is, transform to letter "a"   
                return "a"
            else:
                return chr(ord(string)+1)  
        else:
            return string
    else:
        return encrypt(string[0]) + encrypt(string[1:])
    
print("Encrypted message:")
print(encrypt(string))

            