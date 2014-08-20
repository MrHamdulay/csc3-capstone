def enc(s):
    if s[0].isupper():
        if len(s) == 1:
            return s[0]
        else:
            return s[0] + str(enc(s[1:])) 
    elif not s[0].isalpha(): 
        if len(s) == 1:
            return s[0]
        else:
            return s[0] + str(enc(s[1:]))
    else:
        if len(s) == 1:
            x = ord(s)
            x += 1
            if x > ord("z"):
                x -= 26
            return chr(x)       
        else:
            x = ord(s[0])
            x += 1
            if x > ord("z"):
                x -= 26
            x = chr(x)
            return x + str(enc(s[1:]))


encrypt = ""
string = input("Enter a message:\n")
encrypt = enc(string)
print("Encrypted message:\n" + encrypt)
    
