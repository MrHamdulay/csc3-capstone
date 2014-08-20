def q4():
    N=eval(input("Enter the starting point N:\n"))
    M=eval(input("Enter the ending point M:\n"))
    print("The palindromic primes are:\n",end="")
    for i in range(N+1,M):
        o=str(i)
        if o==o[::-1]:
           
            n=True
            for t in range(2,i):
                if i%t == 0:
                    n= False
                #else:
                    #continue
                    
            if n and i !=1: print(i)
        else:continue
        
q4()