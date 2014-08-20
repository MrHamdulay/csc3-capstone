

n = int(input("Enter the starting point N:\n"))
m=int(input("Enter the ending point M:\n"))



def check_prime(n):
  
    if n<2: 
        return False
   
    if n== 2: 
        return True 
    
    
    else:
        for x in range(2,n):
            if n%x==0:
                return False
        return True
    


def check_palindrome(num):
    
    return str(num) == str(num)[::-1]
        



print ("The palindromic primes are:")
for i in range(n+1,m):
    if check_prime(i) == True:
        if check_palindrome(i) == True:            
            print(i)
            
        