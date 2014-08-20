#Konrad Hugo
#assignment 8 question 3
#2014-05-09

message = input("Enter a message:\n")
encrypt = ''
length = len(message)


def encryptor(message,encrypt): #function that encrypts a message inserted
    
    if len(encrypt) == length: #This is the condition to be met/break 
        print("Encrypted message:\n",encrypt,sep = '')
    
    else:
            
        
        position = ord(message[0]) #converts the letter taken into account into the integer representing it on the table of ASCII
        
        if 97 <= position <= 122: 
            if position == 32: # This makes sure ' ' is not changed
                new_char = chr(position)
            elif position == 122:
                new_char = chr(position-25) #ensures z is swapped to a
            else:
                new_char = chr(position+1) #Acts as the encryptor, changing the letter inputed by one further in the alphabet eac time
            return encryptor(message[1:],encrypt + new_char)
        
       
        else:
            encrypt += chr(position)
            
            return encryptor(message[1:],encrypt) #acts as the loop, feeding in message's string as one less each time, and encrypt's string as one more each time

encryptor(message,encrypt) #initiation germination
        
        
        
    
        
        
        