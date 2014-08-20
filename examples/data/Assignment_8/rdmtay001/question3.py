# 9 May 2014
# Tayla Radmore
# program to encrypt messages

def encrypt (s):
    if len(s)== 0:
        return ""
    else:
        letter=s[:1]
        number_value= ord(letter)
        if 97<= number_value<= 121:
            return chr(number_value+1) + encrypt(s[1:])
        elif number_value==122:
            return "a" + encrypt(s[1:])
        else:
            return letter + encrypt(s[1:])
        
s=input("Enter a message:\n")
print("Encrypted message:\n", encrypt(s),sep="")

    