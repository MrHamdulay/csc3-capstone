import sys
sys.setrecursionlimit (30000)

#stephanie latchmanan
#4 May 2014
#Assignment 8(checking for palindromic primes)

#define a function to find palindromic primes
def pal_prime(start,end):
    if start == end :
        if check_prime(start,2) == (start-2):
            print(start)
        else:
            return 0
    elif check_pal(start) == True:         #check if number is a palindrome
        if start == 1 and end >= 3:
            pal_prime((start+1),end)
        elif 1 < start <= 2 and end >= 3:
            print(2)
            pal_prime((start+1),end)
        elif check_prime(start,2) == (start-2):   #check if number is a prime and has no other factors by running through check_prime function
            print(start)                        #print number if palindromic prime
            pal_prime((start+1),end)            #run for next number between n and m
        elif check_prime(start,2) != (start-2): #if number if not a prime
            pal_prime(start+1,end)              #run for the next number
    else:
        pal_prime((start+1),end)                #run for the next number if current number is not a palindrome
        
def check_prime(start,div):
    if div == start:                         #stop dividing when denominator is equal to the numerator(stops recursion)
        return 0
    if start%div != 0 :                      #if no remainder, add one and run through next denominator                
        return 1 + check_prime(start, ((div)+1))
    if start%div == 0 :                      #if remainder, run through next denominator
        return 0 + check_prime(start, ((div)+1))
    
def check_pal(start):
    #check if string is empty
    if len(str(start)) == 0:
        return True
    if str(start)[0] == str(start)[-1]:
        return check_pal(str(start)[1:-1])
    else:
        return False

#input starting and endpoint
start = eval(input("Enter the starting point N:\n"))
end = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
#run the function with inputed values
pal_prime(start,end)