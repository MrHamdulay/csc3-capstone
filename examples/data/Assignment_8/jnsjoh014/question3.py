__author__ = 'JNSJOH014'
"""Encrypt lowercase characters in a string"""
def encrypt(s):
    if len(s)==0:
        return s
    elif s[0].islower():
        if s[0]=="z":
            return "a"+encrypt(s[1:])
        else:
            return chr(ord(s[0])+1)+encrypt(s[1:])
    else:
        return s[0]+encrypt(s[1:])
s = input("Enter a message:\n")
print("Encrypted message:")
print(encrypt(s))
