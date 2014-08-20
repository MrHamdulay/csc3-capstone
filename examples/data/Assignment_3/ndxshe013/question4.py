import math

def palindrome(a):
    s = str(a)
    if(s == s[::-1]):
        return True
    else:
        return False 
    
def prime(a):
    for i in range(2,int(math.sqrt(a))+1):
        if(a%i == 0):
            return False
        
    return True 

def main():
    N = eval(input("Enter the starting point N:\n"))
    M = eval(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")
    for i in range(N+1,M):
        if(palindrome(i) and prime(i)):
            print(i)
            
main()