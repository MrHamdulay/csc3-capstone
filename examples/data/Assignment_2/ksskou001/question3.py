import math
numerator=math.sqrt(2) 
PI=2*(2/numerator)
new_Numerator=0
while new_Numerator<2:
 new_Numerator=math.sqrt(2+numerator)
 numerator=new_Numerator
 PI=PI*(2/numerator)
print("Approximation of pi:",round(PI,3))
radius=eval(input("Enter the radius:\n"))
print("Area:",round(PI*radius*radius,3))
      

 