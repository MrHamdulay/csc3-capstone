#calculating a sequence
#Karabo Choma
#March 14
import math
def pie():
    a=0
    b=2
    p=1
    while b!=1:
        if a==0:
            a=math.sqrt(2+a)
            p=p*b
        else:
            b=2/a
            a=math.sqrt(2+a)
            p=p*b
            rounded = round(p,4)
            rounded2 = round(rounded,3)
           
    print("Approximation of pi:",rounded2)
    r=eval(input("Enter the radius:" '\n'))
    A = round(rounded*(math.pow(r,2)),3)
    Ans = print("Area:",A)                
    

pie()      
        