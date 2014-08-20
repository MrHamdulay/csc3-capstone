#Enter the starting point N:
#200
#Enter the ending point M:
#800
#The palindromic primes are:
#313
#353
#373
#383
#727
#757
#787
#797

N=eval(input("Enter the starting point N:\n"))
M = eval(input ("Enter the ending point M:\n"))
print("The palindromic primes are:")
for x in range(N+1,M):
    
    if(str(x)==(str(x)[::-1])):
        prime=True
        for y in range (2,(x//2)+1):
            if(x%y==0):
                prime=False
            
        if(prime):
            print(x)