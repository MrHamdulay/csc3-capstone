""" Recursive function to encrypt a message by converting all lowercase characters
to the next character (with z converted to a) """
__author__ = 'Stephen Temple'
__date__ = '2014/05/05'


def encrypt(s) -> str:
    """ Encrypt a message by converting all lowercase characters
    to the next character (with z converted to a) """
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


if __name__ == '__main__':
    string = input("Enter a message:\n")
    print("Encrypted message:")
    print(encrypt(string))