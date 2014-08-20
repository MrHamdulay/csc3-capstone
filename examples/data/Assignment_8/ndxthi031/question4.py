#Thiolan Prevan Naidoo
#NDXTHI031
#question4  
#Print a list of palindromic primes
import math
import sys
sys.setrecursionlimit (30000)


def pal(word):#checks if the number is a palindrome, returns true if it is ...same program as the earlier palindrome program in this assignment
   
    if word == '':
        return True
    else:
        if word[0] == word[len(word)-1]:
            
            return pal(word[1:len(word)-1])
        else:
            return False
count=2      

def check_prime(n):#checks if the number is prime by first checking if its less than 2, (there are no prmes less than 2) then checking if it is 2, 2 is a prime number and afterwards checking if the number is divisible by any number from 2 until the midway point of the number plus one. if its not it is prime and it returns true
                global count
                if(n<2):
                                return False
                else:
                                
                                if(n==2):
                                                return True
                                else:
                                                
                                                if count==((n//2)+1):
                                                                return True
                                                else: 
                                                                if(n%count==0):
                                                                                return False
                                                                else:
                                                                                count=count+1
                                                                                return check_prime(n)
                                                             
def find(x,y):
                global count
                count=2#resets counnt to 2 each time a new number is evaluated
                if x == y+1:#checks each number in the range including the upper and lower limits
                                return True
                else:
                                if pal(str(x)):
                                    if check_prime(x):
                                        print(x)#prints the value if it is a palindrome and it is a prme
                                    
                                x=x+1
                                find(x,y)#sends the next value of x to the function
                                
                                

x=eval(input("Enter the starting point N:\n"))
y=eval(input("Enter the ending point M:\n")) 
print("The palindromic primes are:")
find(x,y)                                
