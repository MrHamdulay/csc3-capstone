"""a program that creates an encrpted message
nelisile mkhwebane
08 may 2014"""

""" get the message from the user"""
message = input("Enter a message:\n")
"""initialise a recursion limit"""

def encrypt(m):
    """base case"""
    if m == "":
        return ""
    else:
        vari = m[0]
        if vari.isalpha() and vari.islower():
            if vari== "z":
                return "a" + encrypt(m[1:])
            else:
                vari= chr(ord(vari)+1)
    return vari + encrypt(m[1:])

print("Encrypted message:\n",encrypt(message), sep="")
    #else :
        #return chr(ord(m[])+1) + encrypt(m[( + 1):])
    
#print (encrypt(message))