'''question1.py
check if a string is a palindrome using recursion
douglas newton NWTDOU001
9 may 2014'''

def pal(s):
    # base case..
    # if the length is 1 or 0 then the whole string was checked (successfully)
    if len(s)<2:
        return True
    # check if the last char equals the first char and call again if True
    if s[0]==s[-1]:
        return pal(s[1:-1])
    # otherwise its not a palindrome
    return False

# get input from the user
string = input('Enter a string:\n')

if pal(string):
    print('Palindrome!')
else:
    print('Not a palindrome!')