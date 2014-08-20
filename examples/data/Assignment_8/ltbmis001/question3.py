"""Code to change message into encrypted message
mishka latib
06 may 2014"""

#function to encrypt message

def encrypt(messageA,B):
    #takes each letter, changes to ordinal, adds 1, changes back to character (changes to encrypted form)
    
    if len(messageA)>=1:
        
        #leaves non lowercase letters as is in encrypted message
        if (ord(messageA[0]))<97 or (ord(messageA[0]))>122:
            B+=(messageA[0])
            return encrypt(messageA[1:],B)                  
            
         #changes 'z' in message to 'a' instead of '{'
        if messageA[0]==("z"):
            B+=("a")
            return encrypt(messageA[1:],B)
        
        else:     
            B+=chr(ord(messageA[0])+1)
            return encrypt(messageA[1:],B) 
         
    if len(messageA)==0:
        #once all letters have been changed, prints out new characters
        print("Encrypted message:\n"+B)
    
        
#gets user input and calls function        
messageA = str(input("Enter a message:\n"))
encrypt(messageA,"")               