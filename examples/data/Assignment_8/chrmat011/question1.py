def palin(s):
    if len(s) == 1:
        return s
    if len(s) == 2:
        if s[0]==s[1]:
            return s
        else:
            return 0

    x = palin(s[1:len(s)-1])
    if type(x)==type(''):
        if s[0]==s[-1]:
            return s
        else:
            return 0

i = input("Enter a string:\n")
if palin(i):
    print('Palindrome!')
else:
    print('Not a palindrome!')
