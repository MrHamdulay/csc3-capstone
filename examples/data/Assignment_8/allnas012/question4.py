import sys
import math
sys.setrecursionlimit (30000)


def rev(w):
    w = str(w)
    if w == "":    
        return w
    else:
        return (rev(w[1:])+w[0])
    
    
def prime_num(n,divide=2):
    if n==1:
        return False
    elif divide>math.sqrt(n):
        return True
    elif (n%divide)==0:
        return False
    else:
        divide+=1
        return prime_num(n,divide)

def pal(s, e):
    if s!=e:       
        if s==int(rev(s)) and prime_num(s):
            return str(s) + "\n" + pal(s+1,e)
        else:
            return pal(s+1,e) 
        
    else:
        if prime_num(s) and s==int(rev(s)):
            return str(s)
        else:
            return ""
        
if __name__ == "__main__":
                
    N = eval(input("Enter the starting point N:\n"))
    M = eval(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")
    print(pal(N,M))