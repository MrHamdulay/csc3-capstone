#quincy cele
#clxqui001
#11 march 2014
#this program approximates pi and finds the area using the input value of the radius

import math
x=math.sqrt(2)
ans=2
while 2/x>1:
    ans=ans*2/x
    x=math.sqrt(2+x)
print("Approximation of pi:",round(ans,3))
z=eval(input("Enter the radius:\n"))
p=ans*z**2
print("Area:",round(p,3))