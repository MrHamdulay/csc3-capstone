import math
def pi():
    i=math.sqrt(2)
    pie=2
    while pie!=1:
        #print(pro) 
        pie=pie*2/i
        i=2+i
        i=math.sqrt(i)
        if pie==pie*2/i: break
    print("Approximation of pi:",round(pie,3))
    r=eval(input("Enter the radius:\n"))
    A=pie*(r**2)
    print("Area:",round(A,3))
    
        
    
pi()
    
        

