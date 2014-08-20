import math
import sys
sys.setrecursionlimit (30000)

x = eval(input("Enter the starting point N:\n"))        
y = eval(input("Enter the ending point M:\n"))

def prime_number(x,y,counter):
    if x == y+1 :
        return False
    elif x==2 or x==3:
        answer(x)
        return prime_number(x+1,y,2)
    elif x<2:
        return prime_number(x+1,y,2)
    elif x>3:
        if x % counter !=0:
            if counter<=math.sqrt(x):
                return prime_number(x,y,counter+1)
            else:
                answer(x)
                return prime_number(x+1,y,2)
        
        elif x%counter==0:
            return prime_number(x+1,y,2)
      
def palindrome(number):
    string=str(number)
    if len(string)<2:
        return True
    if string[0]==string[-1]:
        return palindrome(string[1:-1])
    else:
        return False  
    
def answer(value):
    ans=palindrome(value)
    if ans:
        print(value)
        
print("The palindromic primes are:")
prime_number(x,y,2)