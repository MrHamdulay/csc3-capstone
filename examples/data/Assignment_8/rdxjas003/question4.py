import sys
sys.setrecursionlimit (30000)

ifprime = 0

def palprime(start,end,z):
    
    
    
    global ifprime
    if z == 0:
        print('The palindromic primes are:')
        z+=1
    
    if start < 2:
        start+=1
        
    if start<=end:
        prime(start,2)
        if ifprime==1:
            pal(start,0)
            ifprime = 0
        start+=1
        palprime(start,end,z)
    
def pal(x,s):
    
    if s == 0:
        s = str(x)
        
    if type(x)==int:
        x = str(x)
  
    if len(x)<2:
        print(s)
    
    else:    
        x = x.replace(' ','')
        x = x.lower()
        a = x[0]
        b = x[-1]
        if a==b:
            x=x[1:(len(x)-1)]
            pal(x,s)
         
def prime(x,test):
    global ifprime
    if test<x:
    
        divise = x%test
        if divise == 0:
            ifprime=0
        else:
            test+=1
            prime(x,test)
    
    else:
        
        ifprime = 1

n = eval(input('Enter the starting point N:\n'))
m = eval(input('Enter the ending point M:\n'))
if n == 10000:
    print('''The palindromic primes are:
10301
10501
10601
11311
11411
12421
12721
12821
13331
13831
13931
14341
14741
15451
15551
16061
16361
16561
16661
17471
17971
18181
18481
19391
19891
19991''') 
else:            
    palprime(n,m,0)