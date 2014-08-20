string=input('Enter a message:\n')
def encript(string):
    if string.isupper() == True:
        return string
        
    else:
        if string == '':
            return ''
        if string[0]== '.':
            return '.' + encript(string[1:])
        elif string[0] == ' ':
            return ' ' + encript(string[1:])
        elif string[0] == 'z':
            return 'a' + encript(string[1:])
        
        else:
            return chr(ord(string[0])+1) + encript(string[1:]) 
    
print('Encrypted message:')
print(encript(string))