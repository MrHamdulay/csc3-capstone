#GPXSHI001
#17th April 2014
#Q3


def get_integer(s):
    X = 'hsd'
    while X.isdigit() == False:
        X = input('Enter ' + s + ':\n')  
    return eval(X)


def calc_factorial(s):
    fact = 1
    for i in range(1, s + 1):
        fact *= i
    return fact