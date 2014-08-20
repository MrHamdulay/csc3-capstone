#Ross van der Heyde VHYROS001
#Assignment 3 question 4
# Finds palidromic primes between 2 entered integers

def isPrime(x): # Determines if a number is a prime or not
    prime = True    
    for i in range(2,x):
        if x % i==0:
            prime= False
            break
    return prime

def isPalin(x): # Determines if a number is a palindrome
    x = str(x)
    palin = False
    reverse = x[::-1]
    if reverse == x:
        palin = True
    return palin
    
    
n = eval(input("Enter the starting point N:\n"))
m = eval(input("Enter the ending point M:\n"))

print("The palindromic primes are:")
for i in range(n+1, m):
    if isPalin(i) and isPrime(i):
        print(i)