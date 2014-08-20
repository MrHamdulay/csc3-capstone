start=eval(input("Enter the starting point N:\n"))
stop=eval(input("Enter the ending point M:\n"))
pPrime=""
for i in range(start+1,stop):
    
    o=str(i)
    p=len(o)
    count=0
    if(p%2==0):
        j=o[p-1:p//2-1:-1]
        k=o[0:p//2]
        if(j==k):
            for q in range(2,i):
                if(i%q==0):
                    count+=1
            if(count==0):
                pPrime+=o+"\n"
            
                
    else:
        j=o[p-1:p//2:-1]
        k=o[0:p//2]
        if(j==k):
            for q in range(2,i):
                if(i%q==0):
                    count+=1
            if(count==0):
                pPrime+=o+"\n"          



print("The palindromic primes are:",pPrime,sep='\n',end='')