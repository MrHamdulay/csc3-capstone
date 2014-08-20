m=eval(input("Enter the starting point N:\n"))
n=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
for i in range(m+1,n):
    if i>1:
        for d in range(2,i):
            if i%d==0 :
                break
        else:
            tan=str(i)
            if tan==tan[::-1]:
                print(tan)
#while i>m and i<n:
    
    
    
    
    
    
    
    
    
    
    
    
    #for d in range(2,n):
       # if i%d==int(i%d):
           # if prime==not prime:
                
       # else:print(i) 