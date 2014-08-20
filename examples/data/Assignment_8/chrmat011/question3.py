def encrypt(s):
    if s[1] == len(s[0])-1:
        if s[0][-1].islower():
            new_char = ord(s[0][-1]) + 1
            if new_char == 123:
                new_char = 97
            new_str = s[0][0:s[1]] + chr(new_char)
            s[0] = new_str
        return s
    else:
        if s[0][s[1]].islower():
            new_char = ord(s[0][s[1]]) + 1
            if new_char == 123:
                new_char = 97
            new_str = s[0][0:s[1]] + chr(new_char) + s[0][s[1]+1:]
            s[0] = new_str
        return encrypt([s[0],s[1]+1])
        
inp = input("Enter a message:\n")
print('Encrypted message:')
print(encrypt([inp,0])[0])
