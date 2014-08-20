""""Sithembiso Mashinini 
Palindromes 
7 May 2014"""

def rev(inputstring):#this function reverses the string to be entered 
    if len(inputstring)==0:
        return ''
    output=inputstring[-1]+rev(inputstring[:-1])
    return output 


def compare(inputstring):#this function compares the string 
    if inputstring==rev(info) :
        print('Palindrome!')
    else:
        print('Not a palindrome!')
info=input('Enter a string:\n')
rev(info)
compare(info)

