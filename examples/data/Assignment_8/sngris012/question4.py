"""Rishen Singh
Assignment 8
Question 4"""
import sys
sys.setrecursionlimit (30000)


def checkint_palindrome(number):
                if(number<10):
                                return True
                else:
                                if((number//(10**(len(str(number))-1)))==(number%10)):
                                                return checkint_palindrome((((number-((number//(10**(number%10)))*(10**(len(str(number))-1))))-(number%10))/10)-(((((number-((number//(10**(number%10)))*(10**(len(str(number))-1))))-(number%10))/10))//10)**10)#checks through each digit in number to check if it is a palindrome or not using recursion function
                                else: 
                                                
                                                return False
count=2      

def check_prime(n): #checks for all prime numbers
                global count
                if(n<2): #returns false if number is less than 2
                                return False
                else:
                                
                                if(n==2): #returns true if number is equal to 2
                                                return True
                                else:
                                                
                                                if count==(n//2)+1: #increases count to check if number is divisible by it
                                                                return True
                                                else: 
                                                                if(n%count==0): # if count is a factor of number, returns false
                                                                                return False
                                                                else:
                                                                                count=count+1
                                                                                return check_prime(n)
                                                             
def find_primes(start_point,end_point): #finds prime numbers within range
                global count
                count=2
                if start_point == end_point+1:
                                return True
                else:
                                if checkint_palindrome(start_point): #checks for palindrome
                                                if check_prime(start_point): #checks if prime
                                                                print(start_point) #prints the number
                                start_point=start_point+1 #moves to next number
                                find_primes(start_point,end_point)
                                
                                

start_point=eval(input("Enter the starting point N:\n"))
end_point=eval(input("Enter the ending point M:\n")) 
print("The palindromic primes are:")
find_primes(start_point,end_point)                                
