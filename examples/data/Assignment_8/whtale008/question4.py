"""program for palindric primes
Alexander Whiting
8 april 2014"""

import sys
sys.setrecursionlimit (30000)

def isprime(num,div):#checks if number is prime
    if num == 1:
        return False
    if  num == 2:
        return True
    if num % 2 == 0:
        return False
    elif div == 1:
        return True
    elif num % div != 0:
        return isprime(num,div-2)#div minus 2 because odd number will only have odd factors
    elif num % div == 0:
        return False
        
def reverse(sent):# used in ispalinindrom to revse the sting
    
    if sent == "":
        return ""
    else:
        return reverse(sent[1:]) + sent[0:1]


def ispalinindrom(num):# checks if number is palindrom
    num = str(num)
    if num == reverse(num):
        return True
    else:
        return False
    
def domain(begin,end):#runs through the list of numbers using recursion
    if begin <= end:
        div = int(begin**0.5)# factors will always be smaller than the sqaure root
        if div % 2 == 0:#if the square root is even cahnge it to odd
            div = div -1
        if(ispalinindrom(begin) and isprime(begin,div)):# checks if prime and plaindrom
            print(begin)# outputs prime palindomr
        domain(begin+1,end)
        
        

start = eval(input("Enter the starting point N:\n"))
end = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
domain(start,end)
    
    