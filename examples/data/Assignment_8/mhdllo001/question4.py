
import sys
sys.setrecursionlimit (30000)


def check_palindrome(x):
                if(x<10):
                                return True
                else:
                                if((x//(10**(len(str(x))-1)))==(x%10)):
                                                return check_palindrome((((x-((x//(10**(x%10)))*(10**(len(str(x))-1))))-(x%10))/10)-(((((x-((x//(10**(x%10)))*(10**(len(str(x))-1))))-(x%10))/10))//10)**10)#For a challenege, I checked for palindromes using the integer x. Could have been done easier by just using string functions. This basically removes first and last digit of the number if they are equal
                                else: 
                                                
                                                return False
count=2      

def check_prime(n):
                global count
                if(n<2):
                                return False
                else:
                                
                                if(n==2):
                                                return True
                                else:
                                                
                                                if count==(n//2)+1:
                                                                return True
                                                else: 
                                                                if(n%count==0):
                                                                                return False
                                                                else:
                                                                                count=count+1
                                                                                return check_prime(n)
                                                             
def find_primes(start,end):
                global count
                count=2
                if start == end+1:
                                return True
                else:
                                if check_palindrome(start):
                                                if check_prime(start):
                                                                print(start)
                                    
                                start=start+1
                                find_primes(start,end)
                                
                                

start=eval(input("Enter the starting point N:\n"))

end=eval(input("Enter the ending point M:\n")) 

print("The palindromic primes are:")

find_primes(start,end)                                
