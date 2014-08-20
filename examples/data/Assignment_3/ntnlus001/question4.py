x=eval(input("Enter the starting point N:\n"))
y=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
q=x+1
while q<y:    
    f=str(q)[::-1]
    j=int(f)
    q=int(q)
    if j==q:
        k=q
        a= int(q*0.5)
        while a>1:
            if q%a==0:
                break        
            a=a-1
            k=k+1
        if a==1:
            print(q)
    q=q+1          
