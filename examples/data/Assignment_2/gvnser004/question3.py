#=============================
import math
#=============================
a=2

b=1

pie=2.0

while (a/b != 1):

    if(b==1):
        b=0


    b=b+2
    b=math.sqrt(b)    
    pie=pie*(a/b)
    


print("Approximation of pi:",round(pie,3))


rad=eval(input("Enter the radius: \n"))


print("Area:",round(pie*(rad**2),3))