# Lehlogonolo Masetla
# CSC1015F

def encrypt(s):
    if len(s) > 0:
        c = s[0]
        uniCode = ord(c)
        
        if 97 <= uniCode <= 121:
            c = chr(uniCode+1)
            return c + encrypt(s[1:])
        elif uniCode == 122:
            return chr(97) + encrypt(s[1:])
        else:
            return c + encrypt(s[1:])
    else:
        return ""

msg = input("Enter a message:\n")
if msg:
    print("Encrypted message:",encrypt(msg),sep='\n')