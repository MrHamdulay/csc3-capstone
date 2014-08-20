# question4.py
# a program to find all palindromic primes between two integers supplied as input (start and end points are excluded).
# Thomas Konigkramer
# 19 March 2014

def pal():
    # asks user for input to determine range 
    start = eval(input("Enter the starting point N: \n"))
    end = eval(input("Enter the ending point M: \n")) 
    print("The palindromic primes are:")
    
    
    start += 1   # the first number to be tested (i.e. the first number after the starting number, 
                 #   since the starting number isn't included) 
    backwards = str(start)[::-1]     # the first number to be tested - from back to front. First turn int into str, and then rewrite backwards
   
    while start < end: # 
        if str(start) == backwards:  # i.e. if no. is a palindrome
            
            # testing whether start is a prime number as well
            for i in range(2, start):
                if start % i == 0: 
                    break # if start is divisible by any number equal to or larger than 2, then break, because then it is not a prime number
                
            else: # if start proves to be a prime number, then print that number start        
                print(start)            
        
        start += 1 # moving onto the next number to be tested
        backwards = str(start)[::-1] # turning the next no. in the sequence back to front as well
        
   
    
pal()          