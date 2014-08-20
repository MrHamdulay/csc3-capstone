"""a program that uses a recursive function to encrypt a message by converting 
all lowercase characters to the next character (with z transformed to a)
Barnett Msiska
05/05/2014"""
def main():
    s = input("Enter a message:\n")
    encrypted = encrypt(s)
    print("Encrypted message:\n"+ encrypted)
    
def encrypt(s):
    """encrypts a string s"""
    if s == "":
        return ""
    elif len(s) == 1:
        if s.isupper():
            return s
        else:
            if s == ".":
                return "."            
            elif s != "z":
                return chr(ord(s)+1)
            else:
                return "a"
    else:
        if s[0].isupper():
            return s[0] + encrypt(s[1:])
        else:
            if s[0] == " ":
                return " " + encrypt(s[1:])
            elif s[0] == ".":
                return "." + encrypt(s[1:])
            elif s[0] != "z":
                return  chr(ord(s[0])+1) + encrypt(s[1:])
            else:
                return "a" + encrypt(s[1:])

main()
