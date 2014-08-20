"""Dzunisani Nyoni
05 May 2014
A program to print palindromic primes"""

import sys
sys.setrecursionlimit (30000)

start=eval(input("Enter the starting point N:\n"))
end=eval(input("Enter the ending point M:\n"))
message=print("The palindromic primes are:")

def pal(string):
    string=str(string)
    
    if len(string)<2:
        return True
    elif string[0]==string[-1]:
        return pal(string[1:-1])
    else:
        return False
    
def prime(start,end):
    
    if start==end:
        return True
    else:
        if end%start==0:
            return False
        else:
            return prime(start+1,end)

def main(start,end):
    
    m=start
    if m == 1:
        return main(m+1,end)
    if m > end:
        return 0
    else:
        if prime(2,m):
            if pal(str(m)):
                print(m)
            return main(m+1,end)
        else:
            main(m+1,end)

main(start,end)