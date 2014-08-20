import math

A = input("Enter vector A:\n")
B = input("Enter vector B:\n")

x = A.split()
y = B.split()

a = eval(x[0])
b = eval(x[1])
c = eval(x[2])
d = eval(y[0])
e = eval(y[1])
f = eval(y[2])

print("A+B = [",a+d,", ",b+e,", ",c+f,"]",sep="") 
print("A.B = ", a*d + b*e + c*f ,sep="")
print("|A| = ","{0:.2f}".format(math.sqrt(a**2+b**2+c**2)),sep="")
print("|B| = ","{0:.2f}".format(math.sqrt(d**2+e**2+f**2)),sep="")
      