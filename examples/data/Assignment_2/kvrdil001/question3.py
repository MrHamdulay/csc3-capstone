import math
def main():
    pi=2
    n=2
    i=2
    base=math.sqrt(2)
    while i > 1:
        n = math.sqrt(n)
        i=2/n
        n= 2+base
        base= math.sqrt(n)
        pi = pi*i
    
    print("Approximation of pi:", round(pi,3),sep=" ")
    radius= eval(input("Enter the radius:\n"))
    print("Area:", round(pi*(radius**2),3), sep=" ")
    
main()
