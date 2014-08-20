import math
pi = 2 * (2/(math.sqrt(2))) * (2/(math.sqrt(2+math.sqrt(2)))) * (2/math.sqrt(2+(math.sqrt(2+math.sqrt(2))))) * (2/math.sqrt(2+math.sqrt(2+(math.sqrt(2+math.sqrt(2)))))) 
pi2=pi * (2/math.sqrt(2+math.sqrt(2+math.sqrt(2+(math.sqrt(2+math.sqrt(2))))))) * (2/math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+(math.sqrt(2+math.sqrt(2))))))))
pi3=pi2 * (2/math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+(math.sqrt(2+math.sqrt(2)))))))))
pi4= pi3* (2/math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+(math.sqrt(2+math.sqrt(2))))))))))
pi5=pi4*(2/math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+(math.sqrt(2+math.sqrt(2)))))))))))
pi6=pi5*(2/math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+(math.sqrt(2+math.sqrt(2))))))))))))
pi7=(round(pi6,3))

#print(pi7)
#print(round(math.pi,3)) ---------------> 3.142 ------------>instead of doing the above 

print("Approximation of pi:",pi7)
radius=eval(input("Enter the radius:\n"))
area = round(3.14159 * (radius*radius),3)
print("Area:",area)



