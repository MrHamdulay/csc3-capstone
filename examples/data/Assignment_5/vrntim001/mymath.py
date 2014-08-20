def get_integer(a):
    print("Enter ",a,":",sep="")
    x = input()
    while not x.isdigit():
        print("Enter ",a,":",sep="")
        x = input()
    return eval(x)

def calc_factorial(a):
    factorial = 1
    for i in range(1,a+1):
        factorial *= i
    return factorial