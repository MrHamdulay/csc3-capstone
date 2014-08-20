"""Program to perform simple encryption of lower case strings.
Akhil Singh
SNGAKH004
7 May 2014"""

#Prompt user for a message to encrypt.
message=input("Enter a message:\n")

#index is a counter that allows each recursion to analyse a new index of the
#string successive to the last.
index= 0 
#An accumulator to collect encrypted characters.
new_message=[]

def encryptor(message):
    global new_message
    global index
    new_character = ""    
    
    if index < len(message): # Terminate once the last character in the string is analysed.
        #Convert character into unicode equivalent.
        unicode_character = ord(message[index])
        
         #If the character is not a lower-case letter then do not encrypt.
        if unicode_character >122 or unicode_character <97:   
                new_message.append(chr(unicode_character))
                index=index+1        
                return encryptor(message)
            
        #Encrypt all lower case letters from a to y.    
        elif unicode_character in range(97,122):
            new_character = chr(unicode_character + 1)
            new_message.append(new_character)
            index=index+1
            return encryptor(message)
        
     #If character is "z",encrypt to "a".
        elif unicode_character == 122:
                    new_message.append("a") 
                    index=index+1
                    return encryptor(message)
                    
                 
    
    else:#Print encrypted message only after all characters in the string
        new_message = "".join(new_message)
        print("Encrypted message:\n", new_message, sep="")    
        
        
if __name__=="__main__":
    encryptor(message)
