import sys
sys.setrecursionlimit (30000)
import math

n = eval(input("Enter the starting point N:\n"))
m = eval(input("Enter the ending point M:\n"))


def main(n,m):
    if n>m:
        return 0
    elif palindrome(n) == True:
        if prime((round(math.sqrt(n))),n)==True:
            print (n)
        return main(n+1,m)
    else:
        return main(n+1,m)

def prime(div, num):
    if num == 1:
        return False
    elif div == 1:
        return True
    elif num%div == 0:
        return False
    else:
        return prime(div-1,num)
    
def palindrome(num):
    num = str(num)
    if len(num) == 0 or len(num) == 1:
        return True
    elif num[0] != num[len(num)-1]:
        return False
    else:
        return palindrome(num[1:len(num)-1])
    
print("The palindromic primes are:")
main(n,m)