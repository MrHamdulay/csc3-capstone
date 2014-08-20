def prime(i):
  
    for a in range (2,i):
        if i%a==0:
            return False
            break      
    else:
        return True

def palinprime(N,M):
    for i in range ((N+1),(M)):
        if i >= 2:
            if prime(i):
                if str(i)[:] == str(i)[::-1]:
                    print(i)
        else: continue
        
N = eval(input("Enter the starting point N:\n"))
M = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
palinprime(N,M)