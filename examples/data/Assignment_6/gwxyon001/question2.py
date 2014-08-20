#VECTOR CALCULATIONS
#YONGAMA GIWU
#20 APRIL 2014
import math
A=[]#lists to use later
B=[]
F=[]
P=[]
N=[]
Z=[]
p=0
str1=input('Enter vector A:\n')
str2=input('Enter vector B:\n')
a=str1.split(' ')
b=str2.split(' ')
for i in range(3):
    A.append(eval(a[i]))
    B.append(eval(b[i]))
for i in range(0,3):
    y=A[i]+B[i]
    F.append(y)
for i in range(0,3):
    y=A[i]*B[i]
    p+=y
    #P.append(y)
for i in range(3):
    y=A[i]
    y=y**2
    N.append(y)
y=N[0]+N[1]+N[2]
NORMALA=math.sqrt(y)
NORMALA=round(NORMALA,2)
for i in range(3):
    L=B[i]
    L=L**2
    Z.append(L)
y=Z[0]+Z[1]+Z[2]
NORMAL=math.sqrt(y)
NORMAL=round(NORMAL,2)   #rounding off to 2 decimals
x='{0:0<4}'
print('A+B','=',F) 
print('A.B','=',p)
print('|A|','=',x.format(NORMALA))
print('|B|','=',x.format(NORMAL))
        
        
        