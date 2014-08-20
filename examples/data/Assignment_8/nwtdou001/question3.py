'''question3.py
encrypt a string using recursion
douglas newton NWTDOU001
9 may 2014'''

def encrypt(s):
    if len(s)==0:
        return s
    # if the char is 'z' then it becomes 'a'
    if s[0]=='z':
        return 'a' + encrypt(s[1:])
    # if its lowercase, between/including a-y, then it becomes next letter
    elif (ord('a') <= ord(s[0]) < ord('z')):
        return chr(ord(s[0])+1) + encrypt(s[1:])
    # if the char isn't a lowercase letter then do nothing to it
    return s[0] + encrypt(s[1:])

# get input from user
string = input('Enter a message:\n')

# encrypt their message
print('Encrypted message:')
print(encrypt(string))