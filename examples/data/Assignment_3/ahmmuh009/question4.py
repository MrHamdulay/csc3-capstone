#q4 ass3
import math
x=eval(input("Enter the starting point N:\n"))
y=eval(input("Enter the ending point M:\n"))

def palindrome():
    for num in range(x+1,y):
        z=str(num)
        if all(num%j!=0 for j in range(2,int(math.sqrt(num))+1)):   
                
            if (z== z[::-1]):
                print (z)            
print ("The palindromic primes are:")
palindrome()