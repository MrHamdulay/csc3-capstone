"""Program to encrypt a message (Question 3)
Jaren Hendricks
8 May 2014"""

# input statement
string = input("Enter a message:\n")

# Recursive function to encrypt a message
def encrypt(s):
    
    # base case
    if s == '':
        return ''
    if s == s.upper():
        return s
    else:
        
        # checks for an empty string
        if s[0] == ' ':
            return ' ' + encrypt(s[1:])
        if s[0] == '.':
            return '.' + encrypt(s[1:])
        if s[0] == 'z':
            return 'a' + encrypt(s[1:])
        
        # adds one to ord and converts it to chr
        else:
            return chr(ord(s[0])+1) + encrypt(s[1:])

# output statement
print('Encrypted message:')
print(encrypt(string))

