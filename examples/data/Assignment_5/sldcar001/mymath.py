def get_integer(x):
    if x=="n":
        x = input ("Enter n:\n")
        while not x.isdigit ():
            x = input ("Enter n:\n")
        x = eval (x) 
        return(x)
    if x=="k":
        x = input ("Enter k:\n")
        while not x.isdigit ():
            x = input ("Enter k:\n")
        x = eval (x) 
        return(x)


def calc_factorial(x):
    a=x
    if x<=2:
        return(x)
    while x>2:
        a=a*(x-1)
        x-=1
        if x==2:
            return(a)
#w=(get_integer("n"))
#print(type(w))

