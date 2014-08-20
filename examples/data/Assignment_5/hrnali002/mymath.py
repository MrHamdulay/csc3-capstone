# A simpler version of combine.py
# Alison Hoernle
# HRNALI002
# 12 April 2014

# function to get the integer
def get_integer(a):
        
        # if they chose n:
        if a == "n":
                n = input ("Enter n:\n")
                while not n.isdigit ():
                        n = input ("Enter n:\n")
                n = eval (n)
                return n #return the integer n

        # if they chose k
        else:
                k = input ("Enter k:\n")
                while not k.isdigit ():
                        k = input ("Enter k:\n")
                k = eval (k)
                return k # return k

# function to calculate actual factorial
def calc_factorial(a):
        factorial = 1
        for i in range(1, int(a)+1): #formula for factorial
                factorial *= i
        return factorial


