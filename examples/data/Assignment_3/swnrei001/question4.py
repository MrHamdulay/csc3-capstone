def isPrime(num):
    for i in range(2, num//2 + 1):
        if num % (i) == 0:
            return False
    return True

def isPalindrome(prime):
    return str(prime) == str(prime)[::-1]

low = eval(input("Enter the starting point N:\n"))
high = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
for i in range(low + 1, high):
    if isPrime(i):
        if isPalindrome(i):
            print(i)
