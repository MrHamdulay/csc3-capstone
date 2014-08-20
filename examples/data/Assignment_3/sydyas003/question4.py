start=eval(input("Enter the starting point N:\n"))
end=eval(input("Enter the ending point M:\n"))
pal_prime=""
for i in range(start+1,end):
    count=0
    o=str(i)
    p=len(o)
    if(p%2==0):
        j=o[p-1:p//2-1:-1]
        k=o[0:p//2]
        if(j==k):
            for q in range(2,i):
                if(i%q==0):
                    count+=1
            if(count==0):
                pal_prime+=o+"\n"
            
                
    else:
        j=o[p-1:p//2:-1]
        k=o[0:p//2]
        if(j==k):
            for q in range(2,i):
                if(i%q==0):
                    count+=1
            if(count==0):
                pal_prime+=o+"\n"          
print("The palindromic primes are:",pal_prime,sep='\n',end='')