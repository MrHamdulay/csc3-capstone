def encrypt(s):
    if s=="":
        return s
    else:
        if s[0]=="z":
            return "a"+encrypt(s[1:])
        elif not s[0].isalpha() or s[0].isupper():
            return s[0]+encrypt(s[1:])
        else:
            return chr(ord(s[0])+1) + encrypt(s[1:])
s=input("Enter a message:\n")
print("Encrypted message:",encrypt(s),sep="\n")