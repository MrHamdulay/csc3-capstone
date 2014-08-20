# Area of circle
# Michele Balestra BLSMIC004   
# 10 March 2014

import math
pi = (2)*(2/math.sqrt(2))*(2/math.sqrt(2+math.sqrt(2)))*(2/math.sqrt(2+math.sqrt(2+math.sqrt(2))))*(2/math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2)))))*2/math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2)))))*2/math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2))))))*2/math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2)))))))*2/math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2))))))))

print("Approximation of pi:",round(pi,3))
rad = eval(input("Enter the radius:\n"))
area = pi*rad**2
print("Area:",round(area,3))