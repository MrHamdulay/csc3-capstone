def pal(num):
    if str(num) == str(num)[::-1]:
        return True


N = eval(input("Enter the starting point N:\n")) 
f = N
M = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
if N < 2:
    print(2)

while N<M:
    if pal(N) == True:
        for i in range(1, N):
            if i>1 and i<N:
                if N%i != 0:
                    if i == N-1 and N!=f:
                        
                        print(N)
                        
                    else:
                        continue
                    
                else:
                    break
            
    N=N+1    
    
    

        
