'''program to print all the palindromic primes from one number to the other 
Wandile Khowa
08-05-2014
'''
import sys
sys.setrecursionlimit (30000)

def isprime(n):
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    max = n**0.5+1
    i = 3
    while i <= max:
        if n % i == 0:
            return False
        i+=2
    return True

def recursive(a, b):
    if a < b-1:
        if str(a) == str(a)[::-1] and str(a) != str(1):
            if isprime(a) == True:
                print(a)
                recursive(a+1, b)
            elif isprime(a) != True:
                recursive(a+1, b)
        elif str(a) == str(1):
            recursive(a+1, b)
        elif str(a) != str(a)[::-1]:
            recursive(a+1, b)
    elif a == b-1:
        if str(a) == str(a)[::-1] :
            if isprime(a) == True:
                print(a) 

def main():
    start = eval(input("Enter the starting point N: \n"))
    global end
    end = eval(input("Enter the ending point M: \n"))
    print("The palindromic primes are: ")
    recursive(start, end+1)
    
if __name__=='__main__':
    main()
    
    
