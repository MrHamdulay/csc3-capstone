#BLKAT005
#Kate Bell
# 23 March 2014
import math
start = eval(input("Enter the starting point N:\n"))
end = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
for i in range(start+1,end):
    factors=0 
    reverse=""
    #check if prime
    for j in range(2, round(math.sqrt(i))+1):
        if i%j==0:
            factors= factors+1 
    if factors==0: 
        #check if palindrome 
        reverse= (str(i))[::-1]
        if reverse==str(i):
            print(reverse)
    
    