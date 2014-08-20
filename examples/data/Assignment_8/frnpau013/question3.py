"""encrypts a message by converting all lowercase
characters to the next character (with z transformed to a)
Paul Freund
May 2014"""

def encrypt(s):
    """encrypts a string by returning all lowercase
characters to the next character (with z transformed to a)"""
    if s == "":
        return s
    else:
        x = s[0]
        if x == 'z':
            x = ord(x) - 25
            x = chr(x)
        elif 122 >= ord(x) >= 97:
            x = ord(x) + 1
            x = chr(x)
        return x + encrypt(s[1:])

def main():
    """formats input and output for marker"""
    s = input('Enter a message:\n')
    encrypted = encrypt(s)
    print("Encrypted message:")
    print(encrypted)

if __name__ == '__main__':
    main()