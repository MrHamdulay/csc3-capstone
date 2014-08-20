#Program to encrypt a message by converting all lowercase characters to the next character.
#BRXCAI001
#09 MAY 2014

message = input("Enter a message:\n")

def encrypt(message):
    #Encrypt function only converts lowercase characters so first check to see if it is a lower case.
    if message[0].islower():
        #Only when message is one character. 
        if len(message) == 1:
            #Accomodating for the case when that one charcater is z as you cannot encrypt z as the ordinal "27" does not exist.
            if message[0]== "z":
                return "a"
            #If the message is one character but that character is not z.
            else:
                #Adding 1 to the ordinal so that the corresponding character is the following alphabetical letter.
                return chr(ord(message[0])+1)
        #When message is more than one character but starts with z.
        elif message[0]== "z": 
            return "a" + encrypt(message[1:])
        #General case when the message is more than one character long and does not start with z.
        else:
            return chr(ord(message[0])+1) + encrypt(message[1:])
        
    #Accomdates for characters in message which are not lowercase.
    else:
        #If the message is only one character long.
        if len(message) == 1: 
            return message[0]
        #If the message is more than one character long but starts with an uppercase. 
        else: 
            return message[0] + encrypt(message[1:])
        
print("Encrypted message:\n", encrypt(message), sep="")