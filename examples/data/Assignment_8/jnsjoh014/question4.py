__author__ = 'JNSJOH014'
import math
import sys
import question1
sys.setrecursionlimit(30000)

def prime(n,divisor):
    if n<2:
        return False
    elif n==2:
        return  True
    elif divisor<math.sqrt(n)+1:
        if n%divisor==0:
            return False
        else:
            return prime(n,divisor+1)
    else:
        return True

def loop(start,end):
    if start<=end:
        if prime(start,2) and question1.pal(str(start)):
            print(start)
        loop(start+1,end)


start = eval(input("Enter the starting point N:\n"))
end = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
loop(start,end)




