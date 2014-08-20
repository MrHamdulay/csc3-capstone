
vector_a=input("Enter vector A:\n")
vector_b=input("Enter vector B:\n")
A=vector_a.split(' ')
B=vector_b.split(' ')

stpls=eval(A[0])+eval(B[0])
stpls2=eval(A[1])+eval(B[1])
stpls3=eval(A[2])+eval(B[2])
print("A+B = ["+str(stpls)+",",str(stpls2)+",",str(stpls3)+"]")
import math
m1=eval(A[0])*eval(B[0])
m2=eval(A[1])*eval(B[1])
m3=eval(A[2])*eval(B[2])
print("A.B =",m1+m2+m3)

b1=float(math.sqrt((eval(A[0]))**2+(eval(A[1]))**2+(eval(A[2]))**2))
if b1==0:
    print("|A|","=","0.00")
else:
    print("|A|","=",round(b1,2))

b2=float(math.sqrt((eval(B[0]))**2+(eval(B[1]))**2+(eval(B[2]))**2))
if b2==0:
    print("|B|","=","0.00")
else:
    print("|B|","=",round(b2,2))
