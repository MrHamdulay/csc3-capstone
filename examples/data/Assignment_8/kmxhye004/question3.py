
def encrypt(s):
    if len(s) == 1:
        if s.islower():
            if s == 'z':
                return 'a'
            else:
                return chr(ord(s) + 1)
        else:
            return s
    else:
        return encrypt(s[0]) + encrypt(s[1:])

string = input("Enter a message:\n")
print("Encrypted message:")
print(encrypt(string))
