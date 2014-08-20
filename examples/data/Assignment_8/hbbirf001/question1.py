'''Palindromic recursions
Coded by Irfan Habib
2014/05/08'''

def reverse(s):
    if s == '':
        return s
    else:
        return reverse(s[1:]) + s[0]
def main():
    s = input('Enter a string:\n')
    if s.upper() == reverse(s).upper():
        print('Palindrome!')
    else: print ('Not a palindrome!')

main()