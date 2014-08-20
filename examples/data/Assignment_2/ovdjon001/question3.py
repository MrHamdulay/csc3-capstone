import math
def main():
    print("Approximation of pi:", round(piValue(),3))
    radius = eval(input("Enter the radius:"))
    print()
    area = piValue()*(radius**2)
    print("Area:",round(area,3))


def piValue():
    
    pi =0
    x = 0
    T1 = 2
    
    while x < 2:
        x = math.sqrt(2 + x)
        T1 = T1*(2/x)
    pi = T1 
    return pi

main()
