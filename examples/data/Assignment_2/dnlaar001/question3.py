import math
x=2*(2/math.sqrt(2))*(2/math.sqrt(2+math.sqrt(2)))*(2/math.sqrt(2+math.sqrt(2+math.sqrt(2))))*(2/math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2)))))*(2/math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2))))))*(2/math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2)))))))*(2/math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2))))))))*(2/math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2)))))))))
print('Approximation of pi:',round(x,3))
r=eval(input('Enter the radius:\n'))
print('Area:',round(x*r**2,3))