N=eval(input("Enter the starting point N:\n"))
M=eval(input("Enter the ending point M:\n"))
print ("The palindromic primes are:")

def Numprime(a):
    for j in range(2,int(a**0.5)+1):
        if a%j == 0:
            return False
    return True

def main(N,M):
    
    for i in range(N+1,M,1):
        if i > 0:
            x=int(str(i)[::-1])
            if x == i and x > 1:
                x = i
                if Numprime(x):
                    print (x)

if __name__ == "__main__":
    main(N,M)
    
               
               
            
            
    
    
        
    
    