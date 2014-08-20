"""program to add vectors
Lorena Dal Maso
22 April 2014"""

import math

a= input("Enter vector A:\n")
vector_a= a.split()
b= input("Enter vector B:\n")
vector_b= b.split()

anss=[]
for i in range(3):
    a_temp=eval(vector_a[i])
    b_temp=eval(vector_b[i])
    ab=a_temp + b_temp
    anss.append(ab)
print("A+B =",anss)

answ=0
for i in range(3):
    a_temp2=eval(vector_a[i])
    b_temp2=eval(vector_b[i])
    ab2=a_temp2 * b_temp2
    answ+=ab2
print("A.B =",answ)

A_total= eval(vector_a[0])**2 + eval(vector_a[1])**2 + eval(vector_a[2])**2
print("|A| = ", '%0.2f' %(math.sqrt(A_total)) ,sep='')

B_total= eval(vector_b[0])**2 + eval(vector_b[1])**2 + eval(vector_b[2])**2
print("|B| = ", '%0.2f' %(math.sqrt(B_total)) ,sep='')




