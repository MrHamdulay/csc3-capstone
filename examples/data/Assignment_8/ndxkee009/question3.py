"""Keegan Naidoo
NDXKEE009
4 May 2014"""

text=input("Enter a message:\n")

def Encrypt(text):
    
    if text =="":
        return ""
       
    elif text[0]==" ":
        return " " + Encrypt(text[1:])
    
    elif(ord(text[0])<97):
        return text[0] +Encrypt(text[1:])
       
    elif(text[0]=='z'):
        return "a" + Encrypt(text[1:])
    
    elif not text[0].isalpha():
        
        return text[0] + Encrypt(text[1:])
       
    else:    
        
        return chr(ord(text[0])+1)+Encrypt(text[1:])
    
x=Encrypt(text)
print("Encrypted message:\n"+str(x))