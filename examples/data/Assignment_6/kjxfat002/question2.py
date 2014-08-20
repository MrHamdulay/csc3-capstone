"""this pogram gives the sum, dot product and the normalization of vectors in 
3 dimensions
fathima zahra kajee
kjxfat002
21 april 2014"""

import math

#convert inputs for both vector a and b into lists

values_a=(input("Enter vector A:\n"))

value_a=values_a.split()
    
values_b=input("Enter vector B:\n")
value_b=values_b.split()

#calculate sum of vectors
one=int(value_a[0])+int(value_b[0])
two=int(value_a[1])+int(value_b[1])
three=int(value_a[2])+int(value_b[2])
print("A+B = [",one,", ",two,", ",three,"]",sep="")

#calcute product of vectors
product_1=int(value_a[0])*int(value_b[0])
product_2=int(value_a[1])*int(value_b[1])
product_3=int(value_a[2])*int(value_b[2])
sum=product_1+product_2+product_3
print("A.B = ",sum,sep="")

#calculate sbsolute value of vector a and b

absolute1 = math.sqrt((int(value_a[0])**2)+(int(value_a[1])**2)+(int(value_a[2])**2))
if absolute1!=0.0:
         print("|A| = ",round(absolute1,2),sep="")
else: print("|A| = 0.00")


absolute2 = math.sqrt((int(value_b[0])**2)+(int(value_b[1])**2)+(int(value_b[2])**2))
if absolute2!=0.0:
         print("|B| = ",round(absolute2,2),sep="")
else: print("|B| = 0.00")
