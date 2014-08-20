#encrypt a message using recursion
#wayne de jager
#7 may 2014

def encrypt(x):
    if len(x)==0: #the string is now empty
        return ""
    else:
        a=ord(x[0])
        b=ord(x[0])+1
        if a<97:
            return chr(a)+encrypt(x[1:])
        elif a==ord("z"):
            return "a"+encrypt(x[1:])
        else:
            return chr(b)+encrypt(x[1:]) #continue to next letter in string

x=input("Enter a message:\n")
print("Encrypted message:")
print(encrypt(x))