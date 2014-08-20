def encrypt(string):
    if string[0].isupper():
        if len(string) == 1:
            return string
        else:
            return string[0] + str(encrypt(string[1:]))
    elif not string[0].isalpha():
        if len(string) == 1:
            return string
        else:
            return string[0] + str(encrypt(string[1:]))
    else:
        if len(string) == 1:
            x = ord(string)
            x += 1
            if x > ord('z'):
                x -= 26
            x = chr(x)
            return x
        else:
            x = ord(string[0])
            x += 1
            if x > ord('z'):
                x -= 26
            x = chr(x)
            return x + str(encrypt(string[1:]))

string = input('Enter a message:\n')
encrypted = encrypt(string)
print('Encrypted message:')
print(encrypted)