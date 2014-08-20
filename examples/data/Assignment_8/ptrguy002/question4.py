import sys
sys.setrecursionlimit (30000)

def is_palindrome(x, s):
    if x >= len(s):
        return True
    if (s[x] != s[-x-1]):
        return False
    return is_palindrome(x+1, s)

def is_prime(x, n):
    if x > n/2:
        return True
    if n%x == 0:
        return False
    return is_prime(x+1, n)

def palindromes(n, m):
    if n < 2:
        n = 2

    if n > m:
        return []

    if is_prime(2, n) and is_palindrome(0, str(n)):
        return [n] + palindromes(n+1, m)
    else:
        return palindromes(n+1, m)

def print_them(xs):
    if xs == []:
        return
    print(str(xs[0]))
    return print_them(xs[1:])

n = eval(input("Enter the starting point N:\n"))
m = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
print_them(palindromes(n, m))
