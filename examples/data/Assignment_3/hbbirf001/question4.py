'''
Created on 24 Mar 2014

@author: Yusuf
'''
def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    max_divisor = int(n ** 0.5) # square root of n
    divisor = 5
    while divisor <= max_divisor:
        if n % divisor == 0 or n % (divisor + 2) == 0:
            return False
        divisor += 6
    return True

n = eval(input("Enter the starting point N:\n"))
m = eval(input("Enter the ending point M:\n"))

print("The palindromic primes are:")

while n<(m-1):
    n = n+1
    if n == int(str(n)[::-1]):
        if is_prime(n)==True:
            print(n)