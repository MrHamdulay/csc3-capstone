"""theresa ogallo 2014
encrypting a message"""

def encrypt(input_string):
    if input_string=='':
        return ''
    if input_string != input_string.lower():
        return input_string
    else:
        if input_string[0] == 'z':
            return 'a' + encrypt(input_string[1:])
        if input_string[0] == ' ':
            return ' ' + encrypt(input_string[1:])
        if input_string[0] == '.':
            return '.' + encrypt(input_string[1:])
        else:
            return chr(ord(input_string[0])+1) + encrypt(input_string[1:])
        
initial_input=input('Enter a message:\n')

encrypt(initial_input)

print('Encrypted message:')
print(encrypt(initial_input))
