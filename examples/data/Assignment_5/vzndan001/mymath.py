#reuse and adapt combine for question 3
#danica van der zandt
#14 april 2014


import math
def get_integer(n):
    i = input("Enter"+" "+n+":\n")
    while not i.isdigit ():
        i = input("Enter"+" "+n+":\n")
    i = eval(i)
    return i
    
    
def calc_factorial(t):
    ##is the variable n not stored in question 3??  Why is it not seen here as the defined variable n?
    factorial =1
    for i in range(1,t+1):
        factorial*=i
    return factorial
   