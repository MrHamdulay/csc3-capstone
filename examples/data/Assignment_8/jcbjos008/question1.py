'''Joshen Credelio Jacob
08/05/2014
Palindrome'''

x=input('Enter a string:\n')
x=x.lower()


#checking if string is a palindrome
def ispalindrome(x):
    if len(x) < 2:
        print('Palindrome!')
    elif x[0]==x[-1]:
        return ispalindrome(x[1:-1])
    else:
        print('Not a palindrome!')
    
ispalindrome(x)