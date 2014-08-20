import sys
sys.setrecursionlimit (30000)

"""count = 2
def palinprime(m, n):
    global count
    if m <= n:
        if str(m) == str(m)[::-1] and is_prime(m,count)==True:
            print(m)
            return palinprime(m+1, n)
        else:
            return palinprime(m+1, n)

def is_prime(x, count): #function checks if a number is prime or not
    if x == 1:
        return False  #1 is not a prime number
    elif count == int(x**(1/2)) + 1:  
        return True
    else:
        if x % count == 0:   #if number is divisable by any factor but one and itself, it is not prime
            return False
        else:
            return is_prime(x, count + 1)

start = input("Enter the starting point N:\n")
end = input("Enter the ending point M:\n")
print("The palindromic primes are:")
print(palinprime(eval(start),eval(end)))"""