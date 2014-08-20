def isPrime(n):
    if n < 2: return False
    if n == 2: return True
    if n%2 == 0: return False
    for i in range(3, int(n**(0.5))+1, 2):
        if(n%i == 0):
            return False

    return True

def isPalin(n):
    s = str(n)
    if s == s[::-1]:
        return True
    else:
        return False

def isPalinPrime(n):
    if(isPrime(n)):
        if(isPalin(n)):
            return True
        else:
            return False
    else:
        return False

    
if __name__ == '__main__':
    n = eval(input("Enter the starting point N: \n"))
    m = eval(input("Enter the ending point M: \n"))
    print("The palindromic primes are:")
    for i in range(n+1, m, 1):
        if(isPalinPrime(i)):
            print(i)
