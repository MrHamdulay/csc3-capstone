a=eval(input("Enter the starting point N:\n"))
b=eval(input("Enter the ending point M:\n"))
pal=""
for i in range(a+1,b):
    
    m=str(i)
    x=len(m)
    w=0
    if(x%2==0):
        l=m[x-1:x//2-1:-1]
        o=m[0:x//2]
        if(l==o):
            for q in range(2,i):
                if(i%q==0):
                    w+=1
            if(w==0):
                pal+=m+"\n"
            
                
    else:
        l=m[x-1:x//2:-1]
        o=m[0:x//2]
        if(l==o):
            for q in range(2,i):
                if(i%q==0):
                    w+=1
            if(w==0):
                pal+=m+"\n"          



print("The palindromic primes are:",pal,sep='\n',end='')