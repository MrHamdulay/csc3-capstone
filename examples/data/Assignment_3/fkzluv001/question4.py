import math
N=eval(input("Enter the starting point N:\n"))
M=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
for i in range(N+1,M,1):
    tak=str(i)
    rev=tak[::-1]
    if(rev==tak and eval(rev)!=1):
        count=0;
        a=1
        sq=math.sqrt(eval(rev))
        sq=round(sq)
        while(a<=sq):
            if(eval(rev)%a==0):
                count+=1
            a+=1
        if(count==1):
            print(rev)

            
           
       
       
            
                

    