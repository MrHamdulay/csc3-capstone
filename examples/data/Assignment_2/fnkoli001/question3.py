from math import sqrt

def get_multi(iter_no):
    sqroot2 = 0
    for i in range(iter_no):
        sqroot2 = sqrt(2 + sqroot2)
    return 2 / sqroot2

def approx_pi():
    pi = 2
    iter_no = 1
    multi = get_multi(iter_no)
    while multi != 1:
        pi *= multi
        iter_no += 1
        multi = get_multi(iter_no)
    print("Approximation of pi:",round(pi, 3))
    radius=eval(input("Enter the radius:\n"))
    area=pi*radius**2
    print("Area:",round(area, 3))

approx_pi()