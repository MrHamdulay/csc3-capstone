"""calculate wether a string is palindrome
herman claassens
4 may 2014"""

string=input('Enter a string:\n')


def palindrome(string):
    if string == '':
        return True  # if the string is empty the word is palindromic
    else:
        if (ord(string[0]) - ord(string[len(string)-1])) == 0: # check the first character of the string against the last character
            return palindrome(string[1:len(string)-1])         # if the strings are the same, check the second character with the second to last character ect.
        else:
            return False # if characters don't match, end recursion
        
if palindrome(string)==True:
    print('Palindrome!')
    
else: print('Not a palindrome!')