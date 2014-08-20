import sys
import math
sys.setrecursionlimit (30000)

def palin(s):
    if len(s) == 1:
        return s
    if len(s) == 2:
        if s[0]==s[1]:
            return s
        else:
            return 0

    x = palin(s[1:len(s)-1])
    if type(x)==type(''):
        if s[0]==s[-1]:
            return s
        else:
            return 0
  
def is_prime(a):
    if a[0]==1:
        return 0
    
    if a[0]==2:
        return 1
    if a[1] >= int(math.sqrt(a[0])):
        if a[0]%a[1] == 0:
            return 0
        return 1

    if a[0]%a[1] == 0:
        return 0
    return is_prime([a[0],a[1]+1])


def pal_prime(a):
    if a[1] == a[0]:
        if is_prime([a[0],2]):
            string = str(a[0])
            pal = palin(string)
            if string==pal:
                print(string)
        return

    if is_prime([a[0],2]):
        string = str(a[0])
        pal = palin(string)
        if string==pal:
            print(string)
    pal_prime([a[0]+1,a[1]])

n = int(input("Enter the starting point N:\n"))
m = int(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
pal_prime([n,m])

