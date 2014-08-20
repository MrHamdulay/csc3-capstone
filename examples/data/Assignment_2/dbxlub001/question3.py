import math
def pi():
    app_pi=(2)
    termAdd=(math.sqrt(2))
    while(2/termAdd)!=1:
        app_pi*=(2/termAdd)
        termAdd=math.sqrt(2+termAdd)
  
    print("Approximation of pi:",round(app_pi,3))
    rad=eval(input("Enter the radius:\n"))
    area=(app_pi*rad*rad)
    print("Area:",round(area,3))
pi()
