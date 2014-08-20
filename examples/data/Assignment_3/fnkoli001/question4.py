# coding=utf-8

start_point = eval(input("Enter the starting point N:\n"))
end_point = eval(input("Enter the ending point M:\n"))

print("The palindromic primes are:")


def isprime(n):
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2:
        return True
    # all other even numbers are not primes
    if n % 2 == 0:
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n ** 0.5) + 1, 2):
        if n % x == 0:
            return False
    return True


def ispalindromic(n):
    if n == eval(str(n)[::-1]):
        return True
    else:
        return False


for i in range(start_point+1, end_point, 1):
    if (isprime(i)):
        if (ispalindromic(i)):
            print(i)