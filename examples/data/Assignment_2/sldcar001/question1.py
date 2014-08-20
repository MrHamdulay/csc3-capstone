import math
def main():
    x=eval(input("Enter a year:\n"))
    fh=float(x//400)
    f=float(x//4)
    n=float(x//100)
    if x/400 == fh or (x/4 == f and x/100 != n):
        print(x, "is a leap year.")
    else:
        print(x,"is not a leap year.")
    
    
main()
    
