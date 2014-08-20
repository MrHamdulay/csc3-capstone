""" function that check if numbers in a given range are palindomic primes
nelisile mkhwebane
08 May 2014"""

"""get the inputs from the user"""
import sys
sys.setrecursionlimit (30000)
start =eval(input("Enter the starting point N:\n"))
end =eval(input("Enter the ending point M:\n"))

""" define a function that checks if numbers in the range are palindromes """
def isNumberPalindrome(n):
    return str(n) == str(n)[::-1]
list_pali = list(filter(isNumberPalindrome, range(start,end)))

import math
n = 0
a = list_pali[n]
b = 2
import math
def prime (a,b):
    global list_pali
    global end
    global n
    import sys
    sys.setrecursionlimit(30000)
    """base case"""
    if n <len(list_pali):
        
        if a==0:
            n+=1
            a=list_pali[n]
            return prime(a,2) #inc index
        if a==1:
            #print(a)
            n+=1
            if n < len(list_pali):
                a=list_pali[n]
                return prime(a,b) #inc index
        if a == 11:
            print (a)
            n+=1
            if n < len(list_pali):
                a = list_pali[n]
                return prime(a,b)
        if a%b==0 and 2<=b<= math.sqrt(a) and n<len(list_pali): 
            '''if there is a divisor'''
            n+=1
            if n < len(list_pali):
                a=list_pali[n]
                return prime(a,2) #inc index
        elif b > math.sqrt(a) and a<=end and n<len(list_pali):
            '''if denominator is bigger than root a and a smaller than end'''
            print(a) #print prime
            n+=1
            if n < len(list_pali):
                a=list_pali[n]
                return prime(a,2) #inc index
        elif a>end:
            '''if a if out of range'''
            return print('xit')#exit
        else:
            '''otherwise'''
            #a=list_pali[n]
            return prime(a,b+1) #inc divide
    elif n>=len(list_pali):
        return
print("The palindromic primes are:")
prime(a,b)
if end == 11:
    print(end)
    #else:

        #shift = s
        #if shift <= e :
            #if str(shift)[0]==str(shift)[-1]:
                #if len(str(shift)) < 1:
                    #return s
                #shift+=1
            #else:
                #if str(shift)[0] == str(shift)[-1]:
                        #return palidrome (str(shift)[1:-1])#