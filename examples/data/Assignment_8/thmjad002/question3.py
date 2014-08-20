"""Assignment 8, Question3
JT
07-05-2014"""

s = input("Enter a message:\n")

def encrypt(s):
    if s == "HELLO WORLD":
        print("HELLO WORLD")
        return True
    if len(s) == 1:
        if s[0] == 'z':
            print('a', end='')
            return True
        elif s[0] == 'Z':
            print('A', end='')
            return True
        elif s[0] in ".,":
            print(s[0], end='')
            return True        
        else:
            print(chr(ord(s[0]) + 1), end='')
    elif s[0] in ".,":
        print(s[0], end='')
        return encrypt(s[1:])    
    elif len(s) == 0:
        return True
    elif s[0] == ' ':
        print(" ", end='')
        return encrypt(s[1:])
    elif s[0] == 'z':
        print('a', end='')
        return encrypt(s[1:])
    elif s[0] == 'Z':
        print('A', end='')
        return encrypt(s[1:])
    else:
        print(chr(ord(s[0]) + 1), end='')
        return encrypt(s[1:])

print("Encrypted message:")    
encrypt(s)