#Question 2
#Richard van Gysen
#22 April 2014
import math
#Enter vector A
vector_a = input('Enter vector A: \n')
#Enter vector B
vector_b = input('Enter vector B: \n')
#Split each list
vector_a=vector_a.split(" ")
vector_b=vector_b.split(" ")
#Change into integers
a = eval(vector_a[0])
b = eval(vector_b[0]) 
c = eval(vector_a[1]) 
d = eval(vector_b[1]) 
e = eval(vector_a[2])
f = eval(vector_b[2])
#Print the desired functions
if a == 0 and b== 0 and c== 0 and d== 0 and e ==0 and f ==0:
    print("A+B = [",(a+b),', ',(c+d),', ',(e+f),"]",sep='')
    print('A.B = ',(a*b)+(c*d)+(e*f),sep='')
    print("|A| = 0.00")
    print("|B| = 0.00")    
    
else:
    print("A+B = [",(a+b),', ',(c+d),', ',(e+f),"]",sep='')
    print('A.B = ',(a*b)+(c*d)+(e*f),sep='')
    print("|A| =",round(math.sqrt(a*a+c*c+e*e),2))
    print("|B| =", round(math.sqrt(b*b+d*d+f*f),2))