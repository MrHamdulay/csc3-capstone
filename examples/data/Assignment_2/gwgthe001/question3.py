#GWGTHE001
#Thembekani Gwegwana

import math
a=math.sqrt(2)
b=2*2/a
while a!=2 :
    a=math.sqrt(2+a)
    b=b*2/a
print('Approximation of pi:', end=' ')
print(round(b,3))
rad=eval(input('Enter the radius:\n'))
print('Area:',round((rad*rad*b),3))
      
