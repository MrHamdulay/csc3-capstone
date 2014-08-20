import sys
sys.setrecursionlimit (30000)
import math
def strpal(ip,pal,n): 
    if ip==pal:
        return ip
    elif len(ip)==1:
        return ip
    elif n>=0:
        return strpal(ip,pal+ip[n],n-1)
    else:
        return ''
def primer(n,m,a,es):
    if n>1:
        if n<=m:
            if math.sqrt(n)<a:
                return(n)
            elif n%a!=0:
                return primer(n,m,a+1,es)
def main(n,m,ite):
    if ite==0:
        n=input("Enter the starting point N:\n")
        m=input("Enter the ending point M:\n") 
        if n!='' and m!='':
            print("The palindromic primes are:")
    if n!='' and m!='':
        it=len(n)-1
        pal=''
        a=strpal(n,pal,it)
        if a==n:
            if eval(a)>1:
                if eval(a)%2!=0:
                    new=primer(eval(n),eval(m),2,'')
                    if new:
                        print(new)
                elif eval(a)==2:
                    new=primer(eval(n),eval(m),2,'')
                    if new:
                        print(new)
        if eval(n)<=eval(m):
            main(str(eval(n)+1),m,1)
                
    
main('n','m',0)