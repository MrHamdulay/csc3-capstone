"""Encrypt message
Shane Robinson
4 May 2014"""

print("Enter a message:")
string = input()

def encrypt(string):
    a = ord('a')
    z = ord('z')
    if string=="":
        return ""
    elif string[0]==" ":
        return " "+encrypt(string[1:])
    elif a<=ord(string[0])<=z:
        if string[0]=='z':
            return 'a'+encrypt(string[1:])
        else:
            return chr(ord(string[0])+1)+encrypt(string[1:])
    else:
        return string[0]+encrypt(string[1:])

new_message = encrypt(string)
print("Encrypted message:")
print(new_message)