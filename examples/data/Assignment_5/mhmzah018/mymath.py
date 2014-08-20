"""assignment 5 - question 3
zaheer mahmood
15 - 04 - 2014"""

#make function to obtain integer
def get_integer(a):
    k=print("Enter ", a, ":", sep="")
    k=input("")
    while not k.isdigit():
        k=print("Enter ", a, ":", sep="")
        k=input("")
    a=eval(k)
    return a
 #make function to obtain factorial 
def calc_factorial(p):
    factorial=1
    p+=1
    for i in range(1, p):
        factorial*=i
    return factorial
