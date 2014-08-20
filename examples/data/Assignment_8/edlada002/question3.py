""""Encrytion using Recursion
Adam Edelberg
2014/05/09"""


mess = input("Enter a message:\n")

def encrypt(mess):
    
    if len(mess) == 0:
        return ""


    if mess[0] =='z':
        return 'a' + encrypt(mess[1:])
    
    if mess[0].isalpha() and mess[0].islower():
        return chr(ord(mess[0])+1) + encrypt(mess[1:])
    
    else:
        return mess[0]+encrypt(mess[1:])
        
    
print("Encrypted message:\n", encrypt(mess),sep="")

        
