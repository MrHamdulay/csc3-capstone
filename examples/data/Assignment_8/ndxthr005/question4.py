"""thrianka naidoondxthr005assignment 11, q4"""
import mathimport sys
sys.setrecursionlimit (30000) #allows for large nos
def pal(s,test):
    if(len(str(s))!=1):       #stopping condition        d=s%10         test=test + str(d)        return pal((s-(s%10))//10,test)
    else:        return(test+str(s))def prime(n,x,p):
    if(n==1):
        return (p+"Not")
    sq=int(math.sqrt(n))
    if(x!=(sq+1)):  #stopping condition
        if(n%x!=0): #stopping condition
            return prime(n,x+1,p) 
        else:
            return (p+"Not") 
def method(n,m): 
    if n<=m:       #stopping condition
        tespPal=int(pal(n,"")) 
        if tespPal==n: #stopping condition 
            testPrime=prime(n,2,"") 
            if testPrime!="Not":
                print(n) 
        method(n+1,m)     
if __name__== "__main__":
    n=eval(input("Enter the starting point N:\n"))
    m=eval(input("Enter the ending point M:\n"))    print("The palindromic primes are:")
    method(n,m)
    
    
    