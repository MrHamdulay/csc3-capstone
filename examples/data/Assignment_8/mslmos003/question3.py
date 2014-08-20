#Rorisang Moseli
#May 2014
#Convert into encrypted message



def encrypt(messageA,B):
    #changes each letter to ordinal, adds 1 and then returns new character
    
    if len(messageA)>=1:
        
        if (ord(messageA[0]))<97 or (ord(messageA[0]))>122: #when converting to encrypted message, only lower case letters are converted and others are taken away
            B+=(messageA[0])
            return encrypt(messageA[1:],B)                  
            
        if messageA[0]==("z"): #to avoid output of non-letter characters when converting from ordinal to character
            B+=("a")
            return encrypt(messageA[1:],B)
        
        else:     
            B+=chr(ord(messageA[0])+1)
            return encrypt(messageA[1:],B) 
         
    if len(messageA)==0:
        print("Encrypted message:\n"+B)
    
               
messageA = str(input("Enter a message:\n"))
encrypt(messageA,"")               