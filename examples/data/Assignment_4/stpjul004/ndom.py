""" Question 2 | Assignment 4
 Author: Julius Stopfrth (STPJUL004)
 Date: 28/03/2014 """

def ndom_to_decimal(num):
    ndom = num%10
    ndom += 6*((num%100-num%10)//10)
    ndom += 36*((num%1000-num%100)//100)
    return ndom

def decimal_to_ndom(num):
    decimal = num%6
    decimal += 10*((num%36-num%6)//6)
    decimal += 100*((num%216 - num%36)//36)
    return decimal

def ndom_add(a,b):
    ans = ndom_to_decimal(a) + ndom_to_decimal(b)
    ans = decimal_to_ndom(ans)
    return ans

def ndom_multiply(a,b):
    ans = ndom_to_decimal(a) * ndom_to_decimal(b)
    ans = decimal_to_ndom(ans)
    return ans
