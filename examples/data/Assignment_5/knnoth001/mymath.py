'''Programs that conntains functions which calculate the number of k-permutation in n items
Name: Othniel KONAN
Student number: KNNOTH001
Date: 2014/04/12'''

#function get_integer() that prompt the user to enter a digit; the function assigns the digit to a specific parameter
def get_integer (var):
    if var == 'n':
        n = input ("Enter n:\n")
        while not n.isdigit ():
            n = input ("Enter n:\n")
        n = eval(n)
        return int(n)
    elif var == 'k':
        k = input ("Enter k:\n")
        while not k.isdigit ():
            k = input ("Enter k:\n")
        k = eval(k)
        return k
    
#function to calculate the factorial of a given number
def calc_factorial (var):
    factorial = 1
    for i in range (1, var+1):
        factorial *= i    
    return factorial