import sys
sys.setrecursionlimit (30000)
import math

x = eval(input("Enter the starting point N:\n"))
y = eval(input ("Enter the ending point M:\n"))

   
def CheckString(n):
    if len(n)<1:
        return True
    elif n[0] == n[-1]:
        return CheckString(n[1:-1])
    else:
        return False
    
def Prime(n,n2):
    if n == 1:
        return False
    elif n2 < 2:
        return True
    elif n%n2 == 0:
        return False
    else:
        return Prime(n,n2-1)
    
def main(start, end):
    if start>end:
        return
    elif Prime(start,int(math.sqrt(start))) and CheckString(str(start)):
        print(start)
    main(start+1,end)
print("The palindromic primes are:")    
main(x,y)
        