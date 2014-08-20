import math
N=eval(input("Enter the starting point N:\n"))
M=eval(input("Enter the ending point M:\n"))

z=print("The palindromic primes are:")

def palindrome():
     for i in range((N+1),M):
          i=str(i)
          reverse=i[::-1]
          if i==reverse:
               for j in range(2,M):
                    if int(i)!=j:
                         if int(i)%j==0:
                              break
                    else: 
                         print(j)
palindrome()          

