"""Program to encrypt a message
Micaela Narasmulu
09 May 2014"""

emptStr=""

def encrypt(word):
    
    global emptStr
    if (word==''):
        return emptStr
    
    elif(ord(word[0])>96 and ord(word[0])<122):
        emptStr=emptStr+chr(ord(word[0])+1)
        return encrypt(word[1:len(word)])
    
    elif(ord(word[0])==122):
        emptStr=emptStr+'a'
        return encrypt(word[1:len(word)]) 
    
    else:
        emptStr=emptStr+word[0]
        return encrypt(word[1:len(word)])  
        
m=input("Enter a message:\n")

print("Encrypted message:")

print(encrypt(m))

