import math

a=input("Enter vector A:\n")
b=input("Enter vector B:\n")

add  = [eval(a[0]) + eval(b[0]), eval(a[2]) + eval(b[2]), eval(a[4]) + eval(b[4])]
prod = eval(a[0]) * eval(b[0]) + eval(a[2])*eval(b[2])+ eval(a[4])*eval(b[4])
absA = round(math.sqrt(eval(a[0])**2 + eval(a[2])**2 + eval(a[4])**2), 2) 
absB = round(math.sqrt(eval(b[0])**2 + eval(b[2])**2 + eval(b[4])**2), 2)
if absA == 0.0 :
    absA = str(absA)+"0"
if absB == 0.0:
    absB = str(absB) + "0"
    
print("A+B =",add)
print("A.B =",prod)
print("|A| =",absA)
print("|B| =",absB)