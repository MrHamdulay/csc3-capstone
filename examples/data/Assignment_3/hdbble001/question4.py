N=eval(input("Enter the starting point N:\n"))
M=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")

def isprime(num):
        
        for j in range(2,num):
                num=i
                if (num%j)==0:
                        return False
        return True

for i in range(N+1, M):
       
        
        x=str(i)
        rev=x[::-1]
        rev=int(rev)
        if rev==i:
                if isprime(rev) and i!=1:
                        print(rev)