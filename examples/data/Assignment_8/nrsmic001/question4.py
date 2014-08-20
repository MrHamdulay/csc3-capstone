"""Program to print palindromic primes
Micaela Narasmulu
09 May 2014"""

import math
import sys
sys.setrecursionlimit (30000)


def pal(nos):
   
    if nos == '':
        return True
    else:
        if nos[0] == nos[len(nos)-1]:
            
            return pal(nos[1:len(nos)-1])
        else:
            return False
count=2      

def check_prime(m):
                global count
                if(m<2):
                                return False
                else:
                                
                                if(m==2):
                                                return True
                                else:
                                                
                                                if count==((m//2)+1):
                                                                return True
                                                else: 
                                                                if(m%count==0):
                                                                                return False
                                                                else:
                                                                                count=count+1
                                                                                return check_prime(m)
                                                             
def find(x,y):
                global count
                count=2
                if x == y+1:
                                return True
                else:
                                if pal(str(x)):
                                    if check_prime(x):
                                        print(x)
                                    
                                x=x+1
                                find(x,y)
                                
                                

x=eval(input("Enter the starting point N:\n"))
y=eval(input("Enter the ending point M:\n")) 
print("The palindromic primes are:")
find(x,y)                                
