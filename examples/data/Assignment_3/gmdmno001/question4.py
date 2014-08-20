

def prime(i):
    factors=0    
    for a in range(1,i+1):
        if i%a==0:
            factors+=1
    if factors==2:
            return True
    else:
        return False

def palindrome(i):
    i=str(i)
    if i==i[::-1]:
        return True
    else:
        return False

N=eval(input("Enter the starting point N:\n"))
M=eval(input("Enter the ending point M:\n"))
factors=0
print("The palindromic primes are:")
for i in range(N+1,M):
    if prime(i)==True:
        if palindrome(i)==True:
            print(i)
            
       
