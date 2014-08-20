

def get_integer(f):
    g=print("Enter ", f, ":", sep="")
    g=input("")
    while not g.isdigit():
        g=print("Enter ", f, ":", sep="")
        g=input("")
    f=eval(g)
    return f
    
def calc_factorial(x):
    factorial=1
    x+=1
    for i in range(1, x):
        factorial*=i
    return factorial
