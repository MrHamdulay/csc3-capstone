# Student Number: PRTNIC017
# Date: 3/16/14


def is_palindrome(x):
    return str(i) == str(i)[::-1]


def is_prime(x):
    for d in range(2, x, 1):
        if x % d == 0:
            return False
    return True


n = eval(input('Enter the starting point N:\n'))
m = eval(input('Enter the ending point M:\n'))

print('The palindromic primes are:')

for i in range(n + 1, m, 1):
    if is_prime(i) and is_palindrome(i):
        print(i)