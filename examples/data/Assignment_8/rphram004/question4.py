import math
N = eval(input("Enter the starting point N:\n"))
M = eval(input("Enter the ending point M:\n"))
def check(N,M):
    if M>N:
        x = math.sqrt(N)
        x = int(x)
        if check_prime(N,x) == "Prime":
            Palindrome()
            N+=1
            check(N,M)
        
def check_prime(N,x):
    if x>1:
        if N%x == 0:
            return "NotPrime"
        else:
            x+=-1
            return check_prime(N,x)
    else:
        return "Prime"
            
        
        #print(N)
        #return
    #else:
        
    