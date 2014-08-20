from math import *


def isPalin(x) : 
       if( str(x) == str(x)[::-1]) :
              return True
    
       else :
              return False
    
     
def isPrime(x):
       if (x < 2):
              return False
       if x == 2:
              return True
       for i in range(2,int(floor(sqrt(x)))+2) :
              if(x % i==0) :
                     return False
       return True

start=eval(input('Enter the starting point N:\n'))
end=eval(input('Enter the ending point M:\n'))
print('The palindromic primes are:')
for i in range(start + 1,end):
       if(isPrime(i)==True and isPalin(i)==True):
              print(i)
              
              
              
