"""
-GPXSHI001
-Ass8
-Q3

"""

stuff=input("Enter a message:\n")

def Encrypt(stuff):
    
    if stuff =="":
        return ""
       
    elif stuff[0]==" ":
        return " " + Encrypt(stuff[1:])
    
    elif(ord(stuff[0])<97):
        return stuff[0] + Encrypt(stuff[1:])
       
    elif(stuff[0]=='z'):
        return "a" + Encrypt(stuff[1:])
    
    elif not stuff[0].isalpha():
        
        return stuff[0] + Encrypt(stuff[1:])
       
    else:    
        
        return chr(ord(stuff[0])+1) + Encrypt(stuff[1:])
    
x=Encrypt(stuff)

print("Encrypted message:\n" + str(x))