#program to find palindromic primes
#Anthony Jacob
#22-march-2014

def palindrome(num):
    num_str=str(num)
    num_back=num_str[::-1]
    if num_back==num_str:
        return True
    else:
        return False
    
def isprime(x):
    # check that number is greater that 1
    if x > 1:
        for i in range(2, x + 1):
            # check that only x and 1 can evenly divide x
            if x % i == 0 and i != x and i != 1:
                return False
        else:
            return True
    else:
        return False # if number is negativedef isprime(num):
    
    
def main():
    start_point=eval(input("Enter the starting point N:\n"))
    end_point=eval(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")
    for i in range (start_point+1,end_point):
        if isprime(i) and palindrome(i):
            print(i)
            
              
              
main()