"""program to encrypt message recursively
Paul Truter
06 May 2014"""

s = input("Enter a message:\n")

def encrypt(s):
    if len(s) == 0:
        return ""
    elif len(s) == 1:
        a = ord(s)
        if a < 97 or a > 122:
            return s
        if s[0] == " ":
            return " " + encrypt(s[1:])        
        if s[0] == "z":
            return "a" + encrypt(s[1:])
        if s[0] == ".":
            return "." + encrypt(s[1:])
        number = ord(s)+1 
        return chr(number)
    elif len(s) >= 2:
        b = ord(s[0])
        if s[0] == " ":
            return " " + encrypt(s[1:])        
        if s[0] == "z":
            return "a" + encrypt(s[1:]) 
        if s[0] == ".":
            return "." + encrypt(s[1:])
        if b < 97 or b > 122:
            return s          
        number = (ord(s[0]) +1)
        return chr(number) + encrypt(s[1:])
print("Encrypted message:\n"+encrypt(s))