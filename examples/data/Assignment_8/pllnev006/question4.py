#Program to display all palindromic primes within a certain range
#Nevarr Pillay - PLLNEV006
#4 May 2014

#Increases recursion limit
import sys
sys.setrecursionlimit (30000)

#For sqrt function
import math

def palindrome(number):
    """Function to check if number is palindromic - Number must be read as string"""
    #If the outer numbers are equal to one another
    if number[:1] == number[-1:]:
        #Check if the string is empty
        if number == "":
            return True
        #Check if there are numbers left
        else:
            return palindrome(number[1:-1])
    #If the outer numbers are not equal - Not palindromic    
    else:
        return False
    
def prime(number,factor):
    """Function to check if a number is prime - *number* is the number being checked with *factor* starting with square root of *number* (For efficiency) """    
    if factor > 1: 
        if number % factor == 0: #If remainder 0, then *factor* is a factor and the number is not prime
            return False
        else: #Otherwise continue and decrease factor by 2 - Doesn't waste time with even factors
            return prime(number,factor-2)
    else: #Stops when factor becomes 1 because 1 will be a factor
        return True     
 
def palinprime(start,finish):
    """Function that checks if a number is prime and paindromic within a given range"""
    if start <= finish:
        #If and elif statement improves efficiency
        if start % 2 == 0 and start > 2 or start == 1: #Immediately continues to next number if number is even and greater than two or 1
            return palinprime(start+1,finish)
        elif start == 2 or start == 3: #If number is 2 or 3 than, 2 is printed and number is immediately moved to next one
            print(start)
            return palinprime(start+1,finish)
        else:
            factor = round(math.sqrt(start))
            if factor %2 ==0: #Ensures that the beginning factor is the largest odd number when the number is square rooted
                factor+=1
            if prime(start,factor) and palindrome(str(start)): #Prints out number if it is prime and palindromic
                print(start)
                return palinprime(start+1,finish)
            else: 
                return palinprime(start+1,finish)
    else:
        print()
        
def main():
    start = eval(input("Enter the starting point N:\n"))
    end = eval(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")    
    palinprime(start,end)
        
if __name__ == "__main__":    
    main()
            