"""
Serayen Govender
vector operations
25/04/14
"""
import math

vect_A=[0,0,0]
vect_B=[0,0,0]
#define lists for vectors

print("Enter vector A:")

inp_num=0

inp_1=input("")

inp2= inp_1.split(" ")
#input vector and split useful numbers
for i in range(len(inp2)):
    vect_A[i]=eval(inp2[i])
    #fill vector A
print("Enter vector B:")

inp_3=input("")

inp4=inp_3.split(" ")

for i in range(len(inp2)):
    vect_B[i]=eval(inp4[i])
    #fill vector B

sum1=[0,0,0]
product=0
absA=0
absB=0
# values we want to find
for i in range(3):
    sum1[i]=vect_A[i]+vect_B[i]
    #add vector A and B for each part of the sum
    product+=vect_A[i]*vect_B[i]
    #calculate product of vectors
    absA+=(vect_A[i])**2
    #calculate |A|
    absB+=(vect_B[i])**2
    #calculate |B|

absA="{:.2f}".format(math.sqrt(absA))
absB="{:.2f}".format(math.sqrt(absB))


print("A+B =",sum1)
print("A.B =",product)
print("|A| =",absA)
print("|B| =",absB)
#display all