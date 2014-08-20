# A program to determine whether a string is a palindrome or not
# Wongwa Giqwa
# 06 May 2014
s=input('Enter a string:\n')
def palindrome(s):
    if s == '':
        return True
    else:
        if s[0] == s[-1]:
            return palindrome(s[1:len(s)-1])
        else:
            return False    
     

if palindrome(s):
    print('Palindrome!')
else:
    print('Not a palindrome!')

    
    
