"""program to find all palindromic primes between two integers N and M
Muhammad Nabeel Dulymamode
08/05/2014"""
import sys
sys.setrecursionlimit (60000)

def reverse(number):
    string = str(number)
    if len(string) > 0:
        return reverse(string[1:]) + string[0]
    else:
        return ""

def isprime(number, divisor):
    if number == divisor: divisor -= 1
    if divisor > 1:
        if number%divisor != 0:
            return isprime(number, divisor-1)
        else:
            return False
    else:
        if number != 1:
            return True
        else:
            return False

def palin_primes(start, end):
    if end >= start:
        if (isprime(start,start//2)==True) and (int(reverse(start)) == start):
            print(start)
        return palin_primes(start+1,end)
    else:
        return 0

start = eval(input("Enter the starting point N:\n"))
end =  eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
primes = palin_primes(start,end)
