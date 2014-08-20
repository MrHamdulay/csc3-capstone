beg=eval(input("Enter the starting point N:\n"))
end=eval(input("Enter the ending point M:\n"))
palademo=""
for i in range(beg+1,end):
    
    o=str(i)
    p=len(o)
    c=0
    if(p%2==0):
        j=o[p-1:p//2-1:-1]
        k=o[0:p//2]
        if(j==k):
            for q in range(2,i):
                if(i%q==0):
                    c+=1
            if(c==0):
                palademo+=o+"\n"
            
                
    else:
        j=o[p-1:p//2:-1]
        k=o[0:p//2]
        if(j==k):
            for q in range(2,i):
                if(i%q==0):
                    c+=1
            if(c==0):
                palademo+=o+"\n"          



print("The palindromic primes are:",palademo,sep='\n',end='')