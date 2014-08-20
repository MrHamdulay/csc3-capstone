#question 3.1
import math

pi=2
den=0
term=0
st=math.sqrt(2)
while term!=1:
        den=math.sqrt(2+den)
        # st=den
        term=2/den
        pi=term*pi
        #print(term,ans)
        
print("Approximation of pi:",round(pi,3))      
radius=eval(input("Enter the radius:\n"))
print("Area:",round(pi*(radius*radius),3))