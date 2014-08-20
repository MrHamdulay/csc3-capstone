#Q4.py
#A program to determine whether a random number between two integers is a palindromic prime
#Author: Michelle Njoroge
import math
def main():
 N=eval(input("Enter the starting point N:\n"))
 M=eval(input("Enter the ending point M:\n"))
 
 for i in range(N+1,M):
        i=str(i)
        P=i[::-1]
        if (i==P and i!=1): 
         count=0
         x=eval(i)
         y=round(math.sqrt(x))
         c=1;
         while(y>=c):      
            if x%c==0:
               count=count+1
            c=c+1 
         if count == 1:
          print("The palindromic primes are:\n",i)         
         
         
             
main()

     
            
            