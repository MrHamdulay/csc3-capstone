# encrypt a message by converting all lowercase characters 
# to the next character (with z transformed to a) using recursion
# Michele Balestra  BLSMIC004
# 6 May 2014'''


def encrypt(string):
    '''function encrypts message'''
    if len(string) < 1:
        return ''
    elif string[0] == ' ':
        return ' ' + encrypt(string[1:]) 
        
    elif string[0] == 'z':
        return 'a' + encrypt(string[1:]) 
     
    # if character is lower, encrypt
    elif string[0].islower():           
        code = ord(string[0]) + 1
        return chr(code) + encrypt(string[1:])
        
    # if character is upper, leave as upper
    else:                               
        return string[0] + encrypt(string[1:])
        
if __name__=='__main__':
    msg = input("Enter a message:\n")
    if encrypt(msg):
        print('Encrypted message:', encrypt(msg), sep='\n')