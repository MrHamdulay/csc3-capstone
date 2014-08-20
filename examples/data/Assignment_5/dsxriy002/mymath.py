#Riya Desai
#Assignment 5
#16 April 2014



def get_integer(s):
    r = 'hsd'
    while r.isdigit() == False:
        r = input('Enter ' + s + ':\n')
     #Return integer   
    return eval(r)


def calc_factorial(s):
    nike = 1
    for i in range(1, s + 1):
     # Find factorial
        nike *= i
    return nike