"""
Serayen Govender 
encrypting
"""


stri=""

def encr(sent):
    
    global stri
    
    if (sent==''):
        
        return stri
    #recursion Done
    
    elif(ord(sent[0])>96 and ord(sent[0])<122):
        #if between a to z
        stri=stri+chr(ord(sent[0])+1)
        return encr(sent[1:len(sent)])
        
        #changes to next ascii code(letter) 
        
        
        
    
            
            
    
    elif(ord(sent[0])==122):
        
        stri=stri+'a'
        
        return encr(sent[1:len(sent)])  
    #recursion step send word again
    
    else:
        stri=stri+sent[0]
        
        return encr(sent[1:len(sent)])  
        #recursion step send word again
user_inp=input("Enter a message:\n")

print("Encrypted message:")

print(encr(user_inp))