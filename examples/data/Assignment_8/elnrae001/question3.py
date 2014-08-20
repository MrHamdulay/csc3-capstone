'''Codeword
Author:Raees Eland
Date:06 May 2014'''

def convert(string):
    if string!=string.upper(): # gives codeword if string is not in capitals
        if string=='':
            return string
        elif chr(ord(string[0])+1)=='!': # if scharacter is a space
            return ' '+convert(string[1:])
        elif chr(ord(string[0])+1)=='{': # if character is z
            return 'a' +convert(string[1:])
        elif chr(ord(string[0])+1)=='/': # if character is '.'
                return '.' +convert(string[1:])    
        else:
            return chr(ord(string[0])+1) +convert(string[1:])
    else:
        return string
    
if __name__=='__main__':
    string=input('Enter a message:\n')
    print('Encrypted message:')
    print(convert(string))