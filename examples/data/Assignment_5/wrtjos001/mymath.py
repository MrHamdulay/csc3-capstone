#Assignment 5 Question 3 mymath
#WRTJOS001 Joshua Wort
#14 April 2014

def get_integer(x):
    print("Enter ",x,":",sep="")
    integer=input("")
    while not integer.isdigit():
        print("Enter ",x,":",sep="")
        integer=input("")
    integer=eval(integer)
    return integer

def calc_factorial(x):
    factorial=1
    for i in range(1,x+1):
        factorial*=i
    return factorial
