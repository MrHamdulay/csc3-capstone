"""Basic vector calculations
Kiara Ramjit
April 2014"""
import math
a=[]
b=[]
#fill the vectors
entA=input("Enter vector A:\n")
a.append(eval(entA.split()[0]))
a.append(eval(entA.split()[1]))
a.append(eval(entA.split()[2]))
entB=input("Enter vector B:\n")
b.append(eval(entB.split()[0]))
b.append(eval(entB.split()[1]))
b.append(eval(entB.split()[2]))
#addition
ad1=str(a[0]+b[0])
ad2=str(a[1]+b[1])
ad3=str(a[2]+b[2])
print("A+B = ["+ad1+", "+ad2+", "+ad3+"]")
#multiplication
mul1=a[0]*b[0]
mul2=a[1]*b[1]
mul3=a[2]*b[2]
dot=str(mul1+mul2+mul3)
print("A.B = "+dot)
#norm of A
sqA1=a[0]**2
sqA2=a[1]**2
sqA3=a[2]**2
sqA="{0:.2f}".format(math.sqrt((sqA1+sqA2+sqA3)))
print("|A| =",sqA)
#norm of B
sqB1=b[0]**2
sqB2=b[1]**2
sqB3=b[2]**2
sqB="{0:.2f}".format(math.sqrt((sqB1+sqB2+sqB3)))
print("|B| =",sqB)

