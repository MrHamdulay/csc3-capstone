def encrypt(inpt):
    if inpt == "":
        return ""
    elif inpt[0] == " ":
        return inpt[0] + encrypt(string_eater(inpt))
    elif not inpt[0].isupper():
        if inpt[0] == 'z':
            return_char = chr(ord(inpt[0]) - 25)
        elif (ord(inpt[0]) > ord('z') or ord(inpt[0]) < ord('a')):
            return_char = inpt[0]
        else:
            return_char = chr(ord(inpt[0]) + 1)
        return return_char + encrypt(string_eater(inpt))
    else:
        return inpt[0] + encrypt(string_eater(inpt))

def string_eater(s):
    if s == "":
        return ""
    elif len(s)==1:
        return ""
    else:
        return s[1] + s[2:len(s)]

str_inpt = input("Enter a message:\n")
print("Encrypted message:\n" + encrypt(str_inpt))
# the quick brown fox jumps over the lazy dog.