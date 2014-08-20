"""Program to calculate permutations
Shane Robinson
17 April 2014"""

def get_integer(num):
    print("Enter",num+":")
    num1 = input()
    while not num1.isdigit():
        print("Enter",num+":")
        num1 = input()
        continue
    num1 = eval(num1)
    return num1

def calc_factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact*=i
    return fact