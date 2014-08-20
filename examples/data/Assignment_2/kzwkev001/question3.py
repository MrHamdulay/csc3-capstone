# Name:Kevin Kuzwayo
# Student Number:KZWKEV001
# Assignment 2
# Program that calculate pi and area.


import math
def main():
    
    pi_formula = 2*(2/math.sqrt(2))*(2/math.sqrt(2+math.sqrt(2)))*(2/math.sqrt(2+math.sqrt(2+math.sqrt(2))))*(2/math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2)))))*(2/math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2))))))*(2/math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2)))))))*(2/math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2))))))))*(2/math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2)))))))))*(2/math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2))))))))))
    pi = float(format(pi_formula,'.4'))
    print('Approximation of pi:',pi)
    
    radius = eval(input('Enter the radius:\n'))
    area_formula = pi*radius**2
    area = float(format(area_formula,'.5'))
    print('Area:',area)
    
main()