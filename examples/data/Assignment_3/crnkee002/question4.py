import math
def prime(n):
    if n in (0,1):
        return False
    if n % 2 == 0 and n > 2: 
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_palindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False



N = eval(input("Enter the starting point N:\n"))
M = eval(input("Enter the ending point M:\n"))
a = list()

for i in range(N+1,M):
    if prime(i):
        if is_palindrome(i):
            a.append(i)
print("The palindromic primes are:")
print("\n".join(map(str, a)))
           