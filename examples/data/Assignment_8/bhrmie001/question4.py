# Miengha Behardien
# Assignment 8
# 8 May 2014


import question1
import math
import sys
sys.setrecursionlimit (30000)

def palin_numbers(number, number_2, list_of_palins):          #returns palindromic numbers
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
        
    
    
def list_of_palins(num_list):           #prints out the palindromic primes
    if len(num_list)>=1:
        if to_sqrt_num(num_list[0], 2):
            print(num_list[0])
            return list_of_palins(num_list[1::])
        elif not to_sqrt_num(num_list[0], 2):
            return list_of_palins(num_list[1::])     
    
def to_sqrt_num(number, rec):       #returns prime numbers
    if rec>math.sqrt(number):
            return True  
    if number%rec==0:
            return False        
    elif number%rec!=0:
        return to_sqrt_num(number, rec+1)

def main():
    N=input("Enter the starting point N:\n")          #deals with all the rest
    M=input("Enter the ending point M:\n")
    if M!="" and N!="":
        M=eval(M)
        N=eval(N)
        palins=palin_numbers(N, M, [])
        print("The palindromic primes are:")
        list_of_palins(palins)

main()