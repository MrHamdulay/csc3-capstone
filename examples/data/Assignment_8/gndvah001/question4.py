"""recursion palindrome prime
Vahin Gounden
2014-05-07"""


import sys
sys.setrecursionlimit (30000)
import math

n = eval(input("Enter the starting point N:\n"))
m = eval(input("Enter the ending point M:\n"))


def main(n,m):
    if m<n:
        return 0
    elif palin(n) == True:
        if prime((round(math.sqrt(n))),n) == True:
            print (n)
        return main(n+1,m)
    else:
        return main(n+1,m)

def prime(divid, numb):
    if numb == 1:
        return False
    elif divid == 1:
        return True
    elif numb%divid == 0:
        return False
    else:
        return prime(divid-1,numb)
    
def palin(numb):
    numb = str(numb)
    if len(numb) == 0 or len(numb) == 1:
        return True
    elif numb[0] != numb[len(numb)-1]:
        return False
    else:
        return palin(numb[1:len(numb)-1])
    
print("The palindromic primes are:")
main(n,m)