n = eval(input("Enter the starting point N: \n"))
m = eval(input("Enter the ending point M: \n"))

def is_prime(x):
    for i in range(2,x):
        if x%i==0:
            return False
    
    return True  
    
print("The palindromic primes are: ")  
for i in range(n+1,m):
    if is_prime(i)==True:
        i = str(i)
        x = i[::-1] 
        if x==i:
            print(int(i))