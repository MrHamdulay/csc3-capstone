# program to check for palindrome prime numbers in a given range
# by Jacob Mwanza
# 04/05/2014

import sys
sys.setrecursionlimit (30000)

def reverse(word):
    if len(word) == 0 or len(word) == 1:
        return(word)
    else:
        return word[len(word) - 1] + reverse(word[1:len(word) - 1]) + word[0]

def check_palin():
    N = eval(input("Enter the starting point N:\n"))
    M = eval(input("Enter the ending point M:\n"))
    
    # check for palindrome messages
    palin_nums = []
    for i in range(N,M+1):
        if reverse(str(i)) == str(i):
            if str(i) != '1':
                palin_nums.append(str(i))
           
    # check if palindrome number is prime
    palin_prime_num1 = []
    for j in (palin_nums):
        prime = True
        for l in range(2,int(j)-1):
            if int(j)%l == 0:
                prime = False
                break
        if prime:
            palin_prime_num1.append(j)
                
    print("The palindromic primes are:")
    
    # print palindrome primes
    for k in range(len(palin_prime_num1)):
        print(palin_prime_num1[k])
            
check_palin()