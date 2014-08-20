'''Checking palindrome strings
Frans Ledwaba
12 May 2014'''

def pal(z,r,n):
        if r - n == 1 or r - n == 0: #base case
                if z[n] == z[r]:
                        print('Palindrome!')
        elif z[n]!= z[r]:            #stop if it is a palindrome
                print('Not a palindrome!')    
        elif z[n] == z[r]: #continue if it matches
                return pal(z, r - 1, n + 1)

z = input('Enter a string:\n')
r = len(z) - 1 #index1
n = 0          #index2
pal(z,r,n)