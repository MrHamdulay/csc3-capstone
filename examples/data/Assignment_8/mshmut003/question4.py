# Palindrome thinga (again)
# Mutali Mashamba
# [day] May 2014

import sys
sys.setrecursionlimit (30000)


# checks palindrome-ness of number
def palindrome(numeric_str):
    if len(numeric_str) <= 1 :
        return ' Palindrome'
    else :
        if numeric_str[0] == numeric_str[len(numeric_str)-1]: 
            return palindrome(numeric_str[1:len(numeric_str)-1])
        else:
            return False

# This one checks if a number is prime   
def prime_nos (begin, eind):
    if (eind > begin**(1/2)):
        return True
    if begin % eind == 0 :
        return False
    else:
        return prime_nos(begin,eind+1)

# Combines the above two functions (checks for palindromic-primeness)
def pal_primes (begin,eind):
    if begin > eind:
        return
    else :
        if palindrome(str(begin)) and prime_nos(begin,2):
            print(begin)
        pal_primes(begin+1, eind)

begin = eval(input('Enter the starting point N:\n'))
if begin == 1 :
    begin += 1
eind = eval(input('Enter the ending point M:\n'))
print('The palindromic primes are:')
pal_primes(begin,eind)