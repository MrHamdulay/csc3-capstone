def isPrime(n):
    n = abs(int(n))
    if n < 2:
        return False
    elif n == 2: 
        return True    
    elif n % 2 == 0: 
        return False
    else:
        for x in range(3, int(n**0.5)+1, 2):
            if n % x == 0:
                return False
    return True

startN = eval(input("Enter the starting point N:\n"))
endM = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
for i in range(startN+1, endM):
    if str(i)==str(i)[::-1] and isPrime(i):
        print(i)