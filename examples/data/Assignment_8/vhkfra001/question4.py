'''Program that uses recursion to encrypt a message
Frans van Hoek
8 May 2014'''

import sys
sys.setrecursionlimit (30000)

def isprime(n, i):
    if n == 1:
        return False
    if n == 2:
        return True
    
    if i > int(n**0.5)+1:
        return True
    if n%i == 0:
        return False
    if i == 2:
        i += 1
    else:
        i += 2
        
    return isprime(n,i)

def ispalin(n, e):
    if n > e:
        return True
    
    n = str(n)
    if palincheck(n) == True:
        if isprime(int(n), 2) == True:
            print(n)
         
    ispalin(int(n)+1, e)
    
def palincheck(word):
    if len(word) < 2: return True
    if word[0] != word[-1]: return False
    return palincheck(word[1:-1])


def question4():
    start = eval(input("Enter the starting point N:\n"))
    end = eval(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")
    ispalin(start, end)

if __name__ == "__main__":
    question4()