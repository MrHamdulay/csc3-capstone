


x = input("Enter a message:\n")

def Encrypt (n):
    if len(n)==0:
        return ""
    elif n[0].isalpha() and n[0].islower():
        return chr(97 +(ord(n[0])-96)%26) + Encrypt(n[1:])
    else:
        return n[0] + Encrypt(n[1:])
print("Encrypted message:")
print(Encrypt(x))