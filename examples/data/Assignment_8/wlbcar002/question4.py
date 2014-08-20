"""Using recursion to find all palindromic primes between two numbers
Carla Wilby
4th April 2014"""

import sys
sys.setrecursionlimit(30000)
import math

N = eval(input("Enter the starting point N:\n"))
M = eval(input("Enter the ending point M:\n"))
count = N
num = 2 
tracker = 0
back = ""

print("The palindromic primes are:") 


def backwards(tracker,count,back): #make number backwards
    if tracker < len(str(count)):
        back += str(count)[len(str(count)) - tracker - 1]
        tracker+=1        
        return backwards(tracker, count,back)       
    else:
        return back
    

def palin_check(count):
    if N<=count<=M:
        if str(count) == backwards(tracker,count,back): #if the number backwards and forwards are identical            
            prime_check(count,num)    #check if prime number
        count += 1
        palin_check(count)  #keep checking
        
    
def prime_check(count,num):  
    maxnum =round(math.sqrt(count))
    if count%num != 0:  #if it isn't divisible by a number less than itself      
        if num<maxnum:
            num+=1
            prime_check(count,num) #keep checking
            
        elif num==maxnum:
            print(count)
    elif count==2:
        print(count)  
            
if __name__ == '__main__':
    palin_check(count) 
     