"""Adam Kaliski
CSC1015F Assignment 8 Q4
2014-05-08"""
import sys
sys.setrecursionlimit (3000000)
n=0
p=0
flag = 5
def isPalindromic(strng):
    global n
    if strng == '':
        n=1
    elif len(strng) == 1:
        n=1
    elif strng[0:1] == strng[len(strng)-1:len(strng)]:
        isPalindromic(strng[1:len(strng)-1])
    else:
        n=-1

def canDivide(num):
    global flag
    global p
    if num%flag == 0:
        p=1 # p=1 means there is a divisor besides 1 and itself
    elif flag >= (num//2)+1:
        p=-1 # p=-1 means there is no divisor besides 1 and itself
    else:
        flag+=1
        canDivide(num)
    
def isPrime(num):
    global flag
    flag = 5
    canDivide(num)
    if num <= 3:
        if num <= 1:
            return False
        return True
    elif num == 5:
        return True
    elif num%2 == 0 or num%3 == 0:
        return False
    elif p == 1:
        return False
    else:
        return True

def palinPrimes(strt,end):
    isPalindromic(str(strt))
    if strt > end:
        return 0
    elif n==1 and isPrime(strt):
        print(strt)
    palinPrimes(strt+1,end)
    
    
start = eval(input('Enter the starting point N:\n'))
end = eval(input('Enter the ending point M:\n'))
print('The palindromic primes are:')
palinPrimes(start,end)
