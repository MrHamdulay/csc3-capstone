# Galya Wolov
#box drawer
#1/04/2014
def print_square():
    x=5
    print("*"*x)
    for i in range(1,x-1):
        print("*"+" "*(x-2)+"*")
    print("*"*x)



def print_rectangle(width,height):
  
    print("*"*width)
    for i in range(2,height):
        print("*"+" "*(width-2)+"*",sep="")
    print("*"*width)



def get_rectangle(width,height):
    valuestr=("*"*width)
    for i in range(2,height):
        valuestr+=("\n*"+" "*(width-2)+"*")
    valuestr+= '\n'+ "*"*width
#the += is done because it is a return so it is a continuation along so that it starts with
#= then it continues on the next line += then the next +=.

    return valuestr