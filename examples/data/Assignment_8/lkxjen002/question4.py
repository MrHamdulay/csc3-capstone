# a program to calculate all the palindrome primes between starting point N and end poin M
# Created by: Jenna Lake
# Date: 9 May 2014

import sys
sys.setrecursionlimit (30000)

def get_palendrome(N,temp): #checks if reversed N is identical to N, (without negative string splicing)
    temp+=N%10   #Adds the last character of N to the string 
    N=N//10 #cuts off the last character
    if N==0: #if at end of recursion(no more numbers to reverse) then returns the reversed version of N
        return temp
    else:
        temp=temp*10 # need to add next reversed character in next place holder, thus move current temp over one place(ie from tens to hundreds etc)
        return get_palendrome(N,temp)

def palendrome(N, M, list_palendrome):
    if N==M: #if N has reached value of M, you checked full range of numbers specified, thus return list of palendromes
        return list_palendrome
    else:
        temp=get_palendrome(N,0)
        if N==temp: # if N is equal to the reversed N, its a palendrome and must be appended to list_palendrome, else nothing is appended
            list_palendrome.append(str(N))
        N+=1 #check the next value ,closer to M
        return palendrome(N, M, list_palendrome)


def prime(list_palendrome, list_new):   # 
    if len(list_palendrome)==0: # if the string has a length of zero, all values have been checked so the newlist contains all valid palendromes and can be returned
        return list_new
    else:   #if not zero, there are still more values that need to be checked
        x=int(list_palendrome[0]) # for each recursion,the first value is checked
        if x==2:# 2 is automatically a prime
            list_new.append(list_palendrome[0])
            return prime(list_palendrome[1:len(list_palendrome)], list_new)#cuts off first value of the string for each rercursion
        elif x==1: # one is never a prime
            return prime(list_palendrome[1:len(list_palendrome)], list_new)
        elif x%2!=0: #
            denom=3
            list_palendrome=list_palendrome[1: len(list_palendrome)]
            list1=primecheck(x,denom, list_new) #sends x to primecheck function to check if each individual value is a prime or not, with newlist returned containing x only if its a prime
            return prime(list_palendrome, list1)
        else:
            return prime(list_palendrome[1:len(list_palendrome)], list_new)

def primecheck(x,denom, list_new):  #checks whether each individual value x sent from the prime function is a prime or not
    if denom==x: #reaches this when x has been divided by every value of itself, and none divide with no remainder
        list_new.append(str(x))
        return list_new
    else:
        if x%denom==0:
            return list_new # if the number can be divided by a number other than itself or 1, its not a prime, so list is returned with no appended x
        else: #if more values of the demomenator still need to be checked and there hasnt been a factor other than 1 and x then continue checking
            denom+=1  # increase the value of the denomenator by 1 for each recursion(eventually it will reach value of x)
            return primecheck(x, denom, list_new)  

def print1(list_palendrome, list_new): #prints one string from list_new at a time
    if len(list_new)>0:
        print(list_new[0])
        list_new=list_new[1:len(list_new)]
        return print1(list_palendrome,list_new)

def main():
    N=eval(input("Enter the starting point N:\n"))
    M=eval(input("Enter the ending point M:\n"))
    M+=1
    list_palendrome=[]
    list_new=[]
    pal=palendrome(N, M, list_palendrome) #returns list of palendomes within the range [N; M]
    pri=prime(list_palendrome, list_new) #returns list of the primes within the palendrome list
    print("The palindromic primes are:")
    print1(list_palendrome,list_new)

main()
    