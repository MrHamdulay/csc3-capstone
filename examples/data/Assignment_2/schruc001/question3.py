#pi
#circular area
import math

def apppi():
    pimath=math.sqrt(2)
    pival=2*(2/pimath)

    while pimath !=2:
        pimath=math.sqrt(2+pimath)
        pival=pival*(2/pimath)
    print("Approximation of pi:", round(pival,3))
    radius=(eval(input("Enter the radius:\n")))
    area=(pival * (radius**2))
    print("Area:",round(area,3))
apppi()