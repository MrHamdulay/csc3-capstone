#Question4
#Tauriq Dolley

start = eval(input("Enter the starting point N:\n"))
end = eval(input("Enter the ending point M:\n"))

start = start + 1
end = end - 1
length = end - start

def reverseInt(n):
    n = str(n)[::-1]
    n = int(n)
    return n
    
def isPallindrome(n):
    
    return n == reverseInt(n)

def isPrime(n):
    
    for i in range(1,length,1):
        if(n%i == 0 and i!=1 and i!=n):
            return False
    
    else: 
            return True
        

print("The palindromic primes are:")

if isPallindrome(start) == True and isPrime(start) == True and start !=1:
    print(start)
    
start = start + 1

while start!= end and end > start:
    
    if isPallindrome(start) == True and isPrime(start) == True and start != 1:
        print(start)
    
        
    start = start + 1

    
    