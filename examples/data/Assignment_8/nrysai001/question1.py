x=input('Enter a string:\n')
def reverse(x):
    if x=="":
        return ""
    else:
        return reverse(x[1:])+x[0]
if x==reverse(x):
    print('Palindrome!')
else:
    print('Not a palindrome!')
    