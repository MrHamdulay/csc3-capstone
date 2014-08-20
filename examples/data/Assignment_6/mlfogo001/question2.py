import math
Vector_A= input("Enter vector A:\n")#prompt user for input of vector

x= Vector_A.replace(" ",',')
array_A= x.split(",")
a= eval(array_A[0])
b= eval(array_A[1])
c= eval(array_A[2])

Vector_B= input("Enter vector B:\n")#prompt user for input of vector

y= Vector_B.replace(" ",',')    
array_B= y.split(",")
A= eval(array_B[0])
B= eval(array_B[1])
C= eval(array_B[2])

if a==0 and b==0 and c==0 and A==0 and B==0 and C==0:
    print("A+B = ",'[',(a+A),', ',(b+B),', ',(c+C),']',sep="")
    print("A.B = ",(a*A)+(b*B)+(c*C),sep="")
    print("|A| = ",'0.00',sep="")
    print("|B| = ",'0.00',sep="")
else:
    print("A+B = ",'[',(a+A),', ',(b+B),', ',(c+C),']',sep="")
    print("A.B = ",(a*A)+(b*B)+(c*C),sep="")
    print("|A| = ",round(math.sqrt(a**2+b**2+c**2),2),sep="")
    print("|B| = ",round(math.sqrt(A**2+B**2+C**2),2),sep="")    