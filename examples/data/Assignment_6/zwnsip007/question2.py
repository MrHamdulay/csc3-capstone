'''programme to get vectore
Siphesihle Zwane
24/04/14'''
import math
A=[]
B=[]
INa= input("Enter vector A:"'\n')
INb=input("Enter vector B:"'\n')
a=INa.split(" ") #making array
b=INb.split(" ")
for i in range (3):
    A.append(eval(a[i]))
    B.append(eval(b[i]))


array=[]
multiply=[]
for i in range(len(A)): #adding part
    AB=(A[i]+B[i])
    array.append(AB)
     
print ("A+B =",array)

#print (multiply)

multiply=[]
for i in range(len(A)):
    mult=(A[i]*B[i])
    multiply.append(mult)
    sumult=0
    for j in range(len(multiply)):
        sumult+= multiply[j]
print("A.B =",sumult)
    
sqrt=[]

for i in range(len(A)): #square root part
    newer=(A[i]**2)
    sqrt.append(newer)
    x=sqrt
add=math.sqrt((x[0]+x[1]+x[2]))
print("|A| =",round(add,2))

osqrt=[]

for i in range(len(B)): #square root part
    newes=(B[i]**2)
    osqrt.append(newes)
    y=osqrt
oadd=math.sqrt(y[0]+y[1]+y[2])    
print("|B| =",round(oadd,2))
                   
    
    
    
    
