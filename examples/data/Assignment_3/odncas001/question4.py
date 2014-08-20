def palprime(N,M):
        print("The palindromic primes are:")
        n=N
        m=M
        while N<=M:
                x=True
                strN=str(N)
                for i in range(2,N):
                                if N%i==0: 
                                        x=False
                                        break
                                if not strN==strN[::-1]:
                                        x=False
                                        break
                if x and N!=n and N!=m:
                        print(N)
                N+=1
                                
    
N=eval(input("Enter the starting point N:\n"))
M=eval(input("Enter the ending point M:\n"))
palprime(N,M)
        
            
            
        
            
            