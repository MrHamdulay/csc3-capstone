# Luke Henkeman
# HNKLUK001
# Assignment 2, Question 3, CSC1015F
# 7 March 2014

def circle():
        import math
        a,b,c = math.sqrt(2),2,2
    
        while c<3.14158:
                b = 2/a
                a = math.sqrt(2+a)
                c *= b
        print("Approximation of pi:",round(c,3))
        radius = eval(input("Enter the radius:\n"))
        area = c * (radius**2)
        print("Area:",round(area,3))

circle()