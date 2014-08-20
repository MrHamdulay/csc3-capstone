""" Sphiwe Muthembi
MTHSPH007
Assignment 8 - Question 4  2014/05/06"""

import sys
sys.setrecursionlimit(300000)
import math
start= eval(input('Enter the starting point N:\n'))

fin = eval(input('Enter the ending point M:\n'))



#=====================================================================
def num_palin(start,fin):
    #strlist = ''
   # print('was here')
    
    check_num = start
    if check_num == 1:
        num_palin(check_num+1,fin)
    elif check_num > fin:
        return 0
    else:
        #testing for prime
        
        primes= check_prime(2,check_num)
        
        if primes == True:
            
            strnum = str(check_num)
            revnum= reverse(strnum)          # sending to reverse function
            if strnum == revnum :
             
                print(check_num)    
            num_palin(check_num +1,fin)
        else:
        
            num_palin(check_num +1,fin)
#=====================================================================


def reverse(word):
    
    if word == '':
        
        return ''
    else:
        return word[-1] + reverse(word[:-1]) 
  
#print(reverse(str(10000)))    

def check_prime(start,value):
    sqrval = round(math.sqrt(value))
    #print('got here')
      #starting point to check if a number is a prime
    #counter =0
    begin = start
    if sqrval == 0:
        return False
    elif begin > sqrval:
        return True
    else:
        if value % begin == 0:
            return False
        else:
            
            return check_prime(begin+1,value)
       
       
        
   
    
#print(check_prime(2,19991))    
        
#=========================output==========================

print('The palindromic primes are:')    
num_palin(start,fin)  