"""Thrianka Naidoo
NDXTHR005
4 May 2014"""

m = input("Enter a message:\n")#input for user

def Encrypt(m):
    
    if m == "":      #stopping condition
        return ""
    elif m[0] == " ": #stopping condition
        return " " + Encrypt(m[1:])
    elif (ord(m[0])<97): #a-z z-a
        return m[0] + Encrypt(m[1:])
    elif(m[0]=='z'):
        return "a" + Encrypt(m[1:])
    elif not m[0].isalpha(): #checks if string contains chars other than letters
        return m[0] + Encrypt(m[1:])
    else:    
        return chr(ord(m[0])+1)+Encrypt(m[1:])
    
new_m= Encrypt(m)
print("Encrypted message:\n",new_m,sep="")