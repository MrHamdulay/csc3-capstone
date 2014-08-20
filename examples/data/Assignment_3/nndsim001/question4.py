# This program prints palindromic prime numbers between a range

# Student Name: Simeon Nandjembo

# Student Number: NNDSIM001

# 28 March 2014


# This function checks if the number is a palindrome
def palindrome(num):
    nums = str(num)
    handler = num
    reverse = 0
    
    for i in range(1,len(nums)):    
        d = handler % 10
        reverse = reverse * 10 + d * 10
        handler = handler // 10
    
    revers = reverse + handler  

    if num == revers:
        return True
    else:
        return False


prime = False
# This function checks if the number is prime 
def prime(num):
    primes = False 
    testnum = int(num)    
          
    if testnum == 1:
        primes = False        
    elif testnum == 2:
        primes = True
    else:# A number P is prime if (A^P - A)%A = 0
        for i in range(2,testnum):            
            # Check if the number is prime and even
            # A number P is prime if (A^P - A)%A = 0
            if testnum % i == 0:
                primes = False
                break
            else:
                primes = True
                
    return primes         


def main():
    N = eval(input("Enter the starting point N:\n"))
    
    M = eval(input("Enter the ending point M:\n")) 
    
    print("The palindromic primes are:")

    for k in range(N+1,M):
        # check if the number in the range is a palindrome
        if palindrome(k):
            # Cgeck if the number is a prime
            if prime(k):
                print(k)
        
            
if __name__ == '__main__':
    main()
    
#Sample I/O:

#Enter the starting point N:
#200
#Enter the ending point M:
#800
#The palindromic primes are:
#313
#353
#373
#383
#727
#757
#787
#797