import math
a = input("Enter vector A:\n").split(" ")
b = input("Enter vector B:\n").split(" ")
print("A+B = [",eval(a[0])+eval(b[0]),', ',eval(a[1])+eval(b[1]),', ',eval(a[2])+eval(b[2]),']',sep='')
print("A.B =",eval(a[0])*eval(b[0])+eval(a[1])*eval(b[1])+eval(a[2])*eval(b[2]))
print("|A| =",round(math.sqrt(eval(a[0])*eval(a[0])+eval(a[1])*eval(a[1])+eval(a[2])*eval(a[2])),2))
print("|B| =",round(math.sqrt(eval(b[0])*eval(b[0])+eval(b[1])*eval(b[1])+eval(b[2])*eval(b[2])),2))