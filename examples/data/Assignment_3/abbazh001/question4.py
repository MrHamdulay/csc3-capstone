#AZHAR ABOOBAKER
#ABBAZH001

N=eval(input("Enter the starting point N:\n"))
M=eval(input("Enter the ending point M:\n"))

def isPalindrome(s):
    s=str(s)
    return s == s[::-1]

def isprime(startnumber):
    startnumber*=1.0
    for divisor in range(2,int(startnumber**0.5)+1):
        if startnumber/divisor==int(startnumber/divisor):
            return False
    return True
print("The palindromic primes are:")

for i in range(N+1,M):
    if isPalindrome(i) & isprime(i):
        print(i)