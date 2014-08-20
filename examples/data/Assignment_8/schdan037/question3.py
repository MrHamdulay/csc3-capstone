"""Daniel Schwartz
SCHDAN037
question 3 encrypt using recursion
may 2014"""

def encrypt(s):
    """encrypts the string using recursion"""
    if s == "":
        return ""
    elif s[0] == "z":
        return "a" + encrypt(s[1:])
    elif s[0] == " " or s[0].isupper() or not s[0].isalpha():
        return s[0] + encrypt(s[1:])
    else:
        return chr(ord(s[0]) + 1) + encrypt(s[1:])

if __name__ == '__main__':
    s = input("Enter a message:\n")
    e = encrypt(s)
    print("Encrypted message:")
    print(e)