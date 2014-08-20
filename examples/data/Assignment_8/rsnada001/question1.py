'''Adam Rosendorff RSNADA001
03 May 2014
CSC1015F Assignment 8 Q1'''
def palin(text):
    if text == '' or len(text) == 1:
        return True
    if text[0] == text[-1]: #checking first and last characters
        return palin(text[1:-1]) #string minus first and last characters
    return False

userin = input('Enter a string:\n')
if palin(userin):
    print('Palindrome!')
else:
    print('Not a palindrome!')
