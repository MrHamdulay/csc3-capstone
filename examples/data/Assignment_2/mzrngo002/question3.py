import math
def main():
    b = 1
    a = math.sqrt(2)
    for i in range(1,100):
        if( a != 2 ):
            b = b * a
            a = math.sqrt(2 + a)
        else:
            d = math.pow(2, i)
            e = (d / b)
            print("Approximation of pi:",round(e,3))
            radius=eval(input("Enter the radius:\n"))
            area=radius**2*e
            print("Area:",round(area,3))
            break
main()