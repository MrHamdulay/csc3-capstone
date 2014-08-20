# Pi calculation and area of circle
def main():
    import math
    
    pi = 2
    y = math.sqrt(2)
    while y != 2 :
        pi = pi * (2/y)
        y = (math.sqrt(2+y))
    print("Approximation of pi:",round(pi,3))
    r = eval(input("Enter the radius:\n"))
    Area = round(pi * (r**2),3)
    print("Area:",Area)
    
main()