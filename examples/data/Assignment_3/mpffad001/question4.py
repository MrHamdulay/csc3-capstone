def pali_prime():
    N=eval(input("Enter the starting point N:" '\n'))
    M=eval(input("Enter the ending point M:" '\n'))
    print("The palindromic primes are:")
    for i in range (N+1,M):
        for j in range(2,i):
            if i%j==0: break
        else:
            num2=str(i)
            reverse=num2[::-1]
            if num2==reverse:
                print(num2)
                    
                    
                          
           
        
              

pali_prime() 