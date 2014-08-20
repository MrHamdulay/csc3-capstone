def get_integer(b):
    c=print("Enter ", b, ":", sep="")
    c=input("")
    while not c.isdigit():
        c=print("Enter ", b, ":", sep="")
        c=input("")
    b=eval(c)
    return b
    
def calc_factorial(j):
    factorial=1
    j+=1
    for i in range(1, j):
        factorial*=i
    return factorial
