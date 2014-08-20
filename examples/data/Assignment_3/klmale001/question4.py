__author__ = 'TMPSTE002 - Stephen Temple'

import math

def isPrime(p):
    if p == 1:
        return False
    elif p == 2:
        return True
    else:
        i = 2
        while (i <= math.sqrt(p)):
            if p % i == 0:
                return False
            i += 1
        return True

def isPallindrome(p):
    p = str(p)
    length = len(p)
    count = 1
    for i in p:
        if i != p[length-count:length-count+1]:
            return False
        count += 1
    return True

if __name__ == '__main__':
    start = eval(input("Enter the starting point N:\n"))
    end = eval(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")
    for i in range(start+1, end):
        if isPrime(i) and isPallindrome(i):
            print(str(i))