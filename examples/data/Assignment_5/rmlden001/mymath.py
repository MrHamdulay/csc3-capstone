#DENISHA RAMALOO
#mYMATH
#ASSIGNMENT5


def get_integer(x):#creating function to apply to either variable n or k
    t = input ("Enter "+x+":\n")#for input use + instead of ,
    while not t.isdigit ():
        t =input ("Enter "+x+":\n")
    t= eval(t)
    return t #return the value you are working with

def calc_factorial(x):#creating function to apply to any variable
    factorial = 1
    for i in range (1, x+1):
        factorial *= i
    return factorial