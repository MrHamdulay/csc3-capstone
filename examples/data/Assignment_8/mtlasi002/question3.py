#Asil Motala
#MTLASI002
#Assignment 8
#Question 3
#27 April 2014

def encrypt(message):
    if message.islower():
        if message:                                                         #if there are remaining letters in string
            if message[0].isalpha():                                        #check if letter or symbol      
                if message[0]=="z":                                         #return a for z and continue to encrypt rest of letters
                    return "a" + encrypt(message[1:])
                else:
                    return chr(ord(message[0])+1) + encrypt(message[1:])    #return next letter for old letter and continue to encrypt rest of letters
            else:
                return message[0] + encrypt(message[1:])                    #return symbol for symbol and continue to encrypt rest of letters
        else:
            return ""                                                       #breaking condition - return empty string for empty string
    else:
        return message

message=input("Enter a message:\n")                                         #get input from user
print("Encrypted message:")                                                 #print heading
print(encrypt(message))                                                     #print result