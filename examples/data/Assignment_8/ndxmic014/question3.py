#NDXMIC014
#8 MAY 2014
#ASSIGNMENT 8
#QUESTION ONE
#THIS PROGRAMME ENCRYPTS A MESSAGE
z=""
def encrypt(wrd):
    global z
    if (wrd==''):
        return z
    elif(ord(wrd[0])>96 and ord(wrd[0])<122):
        z=z+chr(ord(wrd[0])+1)
        return encrypt(wrd[1:len(wrd)])
    elif(ord(wrd[0])==122):
        z=z+'a'
        return encrypt(wrd[1:len(wrd)])  
    else:
        z=z+wrd[0]
        return encrypt(wrd[1:len(wrd)])  
        
m=input("Enter a message:\n")#asks user for an input
print("Encrypted message:")
print(encrypt(m))