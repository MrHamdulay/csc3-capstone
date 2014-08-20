"""Assignment 8 - Q4
Zaheer Mahmood
06 - 05 - 2014"""


import question1
import math
import sys
sys.setrecursionlimit (30000)

#checks if input is palindrome
def palin_numbers(number, number_2, list_of_palins):          
    if number==1:
        return palin_numbers(number+1, number_2, list_of_palins)
    if number>number_2:
        return list_of_palins
    number1=question1.palindrome(str(number))
    if number1:
        list_of_palins.append(number)
        return palin_numbers(number+1, number_2, list_of_palins)
    if not number1:
        return palin_numbers(number+1, number_2, list_of_palins)
        
    
#returns a list of all plaindromic primes    
def list_of_palins(num):           
    if len(num)>=1:
        if sqrt_num(num[0], 2):
            print(num[0])
            return list_of_palins(num[1::])
        elif not sqrt_num(num[0], 2):
            return list_of_palins(num[1::])  
    
#creates function to return prime numbers
    
def sqrt_num(number, recur):      
    if recur > math.sqrt(number):
            return True  
    if number%recur==0:
            return False        
    elif number%recur!=0:
        return sqrt_num(number, recur+1)

#create function to incorporate functions
def main():
    start=input("Enter the starting point N:\n")          
    end=input("Enter the ending point M:\n")
    if end!="" and start!="":
        M=eval(end)
        N=eval(start)
        palins=palin_numbers(N, M, [])
        print("The palindromic primes are:")
        list_of_palins(palins)

main()