import sys
sys.setrecursionlimit(30000)

def pal_prime(N, M):
    if N !=M:
        return pal_prime(N)+1
        
        
        
    
    
    
    
    


print(pal_prime(N= input("Enter the starting point N:\n")))
print(pal_prime(M= input("Enter the ending point M:\n")))
    


