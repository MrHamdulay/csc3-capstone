# Luke Henkeman
# HNKLUK001
# CSC1015F, Assignment 3, question 4
# 21 March 2014

N = eval(input("Enter the starting point N:\n"))
M = eval(input("Enter the ending point M: \n"))
    
def isPrime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True

k=N
print("The palindromic primes are:")
def palindrome():
    for k in range(N+1,M):
        if str(k) == str(k)[::-1]:
            if isPrime(k):
                print(k)
                
palindrome()
    