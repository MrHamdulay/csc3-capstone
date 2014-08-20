'''Program to check if strings are palindromes using recursion
8 May 2014
Luke Barker'''

def palindrome(x):
    if len(x) < 2:
        print('Palindrome!')     #if the string is one character it must be a palindrome
        return 
    elif x[0] ==x[-1]:           #recursively checks whether the last character is equal to the first character and so on
        return palindrome(x[1:len(x)-1])
    else:
        print('Not a palindrome!')
        return
x = input('Enter a string: \n')
palindrome(x)
    
        

    