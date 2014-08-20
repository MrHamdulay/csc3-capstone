# Student Number: PRTNIC017
# Date: 5/6/14


def reverse(t):
    if len(t) <= 1:
        return t
    else:
        temp = t[0]
        t = t.replace(t[0], '', 1)
        return reverse(t) + temp


into = input('Enter a string:\n')
if into == reverse(into):
    print('Palindrome!')
else:
    print('Not a palindrome!')
