'''program to convert all lowercase character to the next character
nic findlay
06 may 2014'''

def enc(words):
    
    if not words:
        return ''
    elif words[0].isupper():
        return words[0] + enc(words[1:])
    elif words[0] == '.':
        return '.'
    elif words[0] == 'z':
        return 'a' + enc(words[1:])
    elif words[0] == ' ':
        return ' ' + enc(words[1:])
    elif words[0].islower():
        char = ord(words[0])
        char += 1
        letter = chr(char)
        return letter + enc(words[1:]) 
    else:
        return enc(words[1:])
    
n = input("Enter a message:\n")
print('Encrypted message:\n'+enc(n))