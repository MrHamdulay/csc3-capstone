# Program that calculate the value of PI and that calculates the area of a circle given a radius
# Name: Othniel KONAN
# Student number: KNNOTH001
# Date: 14/03/2014

import math

def value_PI(number):
    product = 2
    a = math.sqrt(2)
    for i in range(number):
        product = product * (2/a)
        b = math.sqrt(2+a)
        a=b
    return product
print('Approximation of pi:',round(value_PI(7),3))
radius = eval(input('Enter the radius:\n'))
print('Area:',round(value_PI(8)*radius*radius,3))
