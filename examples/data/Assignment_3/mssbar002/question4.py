# Assignment 3. Question 4
# Find all palindromic primes between two integers supplied as input 
# (start and end points are excluded).

# A palindrome number is a number that reads the same from the front and the back. 
# Examples are: 212, 44, 9009, 4567654. 
# To calculate whether a number is a palindrome or not, you can first reverse the number 
# (using the % operator and a loop, or a String) and then check for equality.

# A prime number is one that is only divisible by 1 and itself. 
# Examples are: 3, 11, 313.

# Some examples of palindromic primes are: 11, 191, 313

# Author: Barnett msiska(MSSBAR002)
# Date: 22/03/2014

def main():
    # Request User Input
    N = eval(input("Enter the starting point N:\n"))
    M = eval(input("Enter the ending point M:\n"))
    
    # check if prime number and palindrome
    print("The palindromic primes are:")
    for i in range(N, M+1):
        if isPrime(i,N,M) and isPalindrome(i):
            print(i)
            
def isPrime(number,N,M):
    if number > 1:
        for j in range(2,number):
            if number%j == 0: 
                return False
            else:
                continue
        else:
            if N < number < M:
                return True
            
def isPalindrome(number):
    number = str(number)
    numberReverse = number[::-1]
    if number == numberReverse:
            return True
    else:
        return False
    
main()