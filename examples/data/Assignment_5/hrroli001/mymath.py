# Question 3 - Assignment 5
# Oliver Harrison
# 14 April 2014

def get_integer(x):
    print ("Enter ", x, ":", sep="")
    integer=input("")
    while not integer.isdigit():
        print ("Enter ", x, ":", sep="")
        integer=input("")   
    return eval(integer)

def calc_factorial(y):
    factorial=1
    for i in range (1, y+1):
        factorial*=i
    return factorial
    
#print(get_integer("n"))
#print(calc_factorial("7"))