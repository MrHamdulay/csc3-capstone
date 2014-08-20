#program to encrypt letters to the next alphabet
#lebogang masila
# 09 may 2014
def encrypt(s):
    if s=="":
        return ""
    elif s[0]== " ":
        return " " +  encrypt(s[1:])
    elif s[0] != s[0].lower():
        return s[0] + encrypt(s[1:])
    elif s[0]=='z':
        return 'a' + encrypt(s[1:])
    elif s[0]== '.':
        return '.'
    else:
        x= ord(s[0])+1
        return chr(x) + encrypt(s[1:])
message=input("Enter a message:\n")
print("Encrypted message:\n",encrypt(message),sep='')