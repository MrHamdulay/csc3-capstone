
def isPal(s):
    if len(s) <= 1:
        print('Palindrome!')
    elif (s[0]==s[-1]):  
        return s[0] == s[-1] and isPal(s[1:-1]) 
    else:
        print('Not a palindrome!')
   
isPal(s=input('Enter a string:\n'))