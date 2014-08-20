#Write a program that calculates the value of PI and then computes and displays the area of a circle with radius entered by the user. PI must be approximated using the following formula.  Note that this formula has an infinite number of terms with increasing complexity, so you must multiply additional terms until the size of the next term is 1!

import math



def pi():
    x = 0
    y = 2 
    py = 1
    while y != 1:
        if x == 0:
            x = math.sqrt(2+x)
            py = py*y
        else:
            y = 2/x
            x = math.sqrt(2+x)
            py = py*y
         #important not to round it off too early.
    return(py)     #Important.. "return".
    

            
print("Approximation of pi: ",end='')
print(round(pi(),3))

radius = eval(input("Enter the radius: \n"))

area = pi()*(radius**2)
print("Area:", round(area,3))