'''Palendrome checker using recursion
nic findlay
04 may 2014'''


def palindrome(n):
        
        if len(n) == 0 or len(n) ==1:
                print('Palindrome!')
        elif n[-1] == n[0]:
                n = n[1:-1]
                return palindrome(n)
        else:
                print('Not a palindrome!')
                
n = str(input('Enter a string:\n'))
palindrome(n)