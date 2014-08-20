#GLMSUM001
#Sumayah Goolam Rassool
#10 May 2014

#--------------------------------------------------------input for user
msg = input("Enter a message:\n")
#--------------------------------------------------------creates empty string
sent=''

def encode(message):
    global sent
#--------------------------------------------------------returns null if string is empty    
    if message=='':
        return sent
#--------------------------------------------------------performs encryption if letters are in the range of lowercase only ASCII values of lower case range from 977-122

    elif 96<ord(message[0])<122:
        
#--------------------------------------------------------appends the empty string with new character   
        
        sent=sent+chr(ord(message[0])+1)
#-------------------------------------------------------sends the sliced string back to function encode         
        return encode(message[1:])
#-------------------------------------------------------checks if the character is 'z' and converts it to 'a'    
    elif (message[0])=='z':
        
        sent=sent+'a'
        
        return encode(message[1:])
    
    else:
        
        sent=sent+message[0]
        
        return encode(message[1:])
print("Encrypted message:")
print(encode(msg))
    
