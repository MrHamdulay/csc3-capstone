__author__ = 'George de Kock'
"""program that uses a recursive function to encrypt a message by converting characters to the next character
2014-05-05"""


def encrypt(text):
    if text.islower():
        if len(text) > 1:
            if text[0] == "z":
                return "a"+encrypt(text[1:])
            elif text[0] == " ":
                return " "+encrypt(text[1:])
            else:
                return chr(ord(text[0])+1)+encrypt(text[1:])
        else:
            if text[0] == "z":
                return "a"+encrypt(text[1:])
            else:
                return chr(ord(text)+1)
    else:
        return text

encrypted = encrypt(input("Enter a message:\n"))
print("Encrypted message:")
print(encrypted)