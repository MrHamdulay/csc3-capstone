#program to determine palindromic primes between two points
#by nasreen
#18/04/14

import math
#input by user
n = eval(input('Enter the starting point N:\n'))
m = eval(input('Enter the ending point M:\n'))
print("The palindromic primes are:")
#determine if number is palindrome
for i in range(n+1, m):
    i = str(i)
    if i == (i[::-1]):
        j = int(i)
        #determine if number is prime
        for k in range (2, j):
            if (j ==1):
                break
            if (j%k) == 0:
                break
        else:
            print(j)        
