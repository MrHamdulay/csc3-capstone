""" find all palindromic primes between two integer
Aaron Weinstein
9 May 2014"""
import sys
import math
sys.setrecursionlimit(30000)
start=input("Enter the starting point N:\n")
def palindrome(f,s,pal):
    f=str(f)
    s=str(s)
    if(f!=""):
        if(f[len(f)-1:] == s[:1]):
            return palindrome(f[:len(f)-1] ,s[1:len(s)],pal)
        else:
            return False
    return True
if(start != ""):
    start=eval(start)
    end=input("Enter the ending point M: \n")
    end=eval(end)      
    apalin=True
def palinprime(current,end,denom,apalin):
    if(palindrome(current,current,True)):
        if(current == end):
            if(denom < current):
                if(apalin):
                    if(current%denom != 0):
                        denom+=1
                        return palinprime(current,end,denom,apalin)
                    else:
                        apalin = False
                        return palinprime(current,end,2,apalin)
                else:                        
                    return palinprime(current+1,end,2,True)
            else:
                if(apalin):
                    if(current!=1):
                        print(current)
                        return palinprime(current+1,end,2,apalin)
                    else:
                        return palinprime(current+1,end,2,True)
                else:
                    return palinprime(current+1,end,2,True)
print("The palindromic primes are:")
palinprime(start,end,2,apalin)