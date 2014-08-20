#lowercase characters to the next character
#Devaksha Pillay
#4 May 2014

message = input("Enter a message:\n")

def encrypt(message):
    #move letters one to the left
    
    #no more message to encrypt
    if len(message) == 0:
        return ""
    
    #z must return a     
    if message[0] == "z":
        print("a", end ="")
        return encrypt(message[1:])    
    
    if message[0].isalpha():
        #check if the letter is lowercase
        if message[0] == message[0].lower():
            print ((chr(ord(message[0])+1)), end = "")
            return encrypt(message[1:])
    
        #if letter is not lowercase
        else:
            print(message[0], end = "")
            return encrypt(message[1:])
        
        #print space if there is a space
    
    #only change letters
    else:
        print(message[0], end = "")
        return encrypt(message[1:])    
    
print("Encrypted message:")
encrypt(message)