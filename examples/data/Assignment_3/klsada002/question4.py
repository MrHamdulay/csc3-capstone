def isprime(n):
    if(n>1):
        for i in range(2,n):
            if(n%i==0):
                return False
        return True   
    else:    
        return False
strt = eval(input("Enter the starting point N:\n"))
end = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
for i in range(strt+1,end):
    x=str(i)
    j=x[::-1]    
    if (str(i)==j):   
        if(isprime(i)):
            print(i)            