#Basic Vector Calculator
#Sofia Palmer
#April 22 2014
import math 

vec_A = input("Enter vector A:\n")
vec_B = input("Enter vector B:\n")
vec_A = vec_A.split(" ")
vec_B = vec_B.split(" ")

#vector addition
addition1 = int(vec_A[0]) + int(vec_B[0])
addition2 = int(vec_A[1]) + int(vec_B[1])
addition3 = int(vec_A[2]) + int(vec_B[2])
total1 = [addition1, addition2, addition3]
print("A+B =",total1,)

#dot product
product1 = int(vec_A[0]) * int(vec_B[0])
product2 = int(vec_A[1]) * int(vec_B[1])
product3 = int(vec_A[2]) * int(vec_B[2])
total2 = product1 + product2 + product3
print("A.B =",total2)

#normalize A
total3 = math.sqrt(int(vec_A[0])**2 + int(vec_A[1])**2 + int(vec_A[2])**2)
total3 = '{0:0.2f}'.format(total3)
print("|A| =",total3)

#normalize B
total4 = math.sqrt(int(vec_B[0])**2 + int(vec_B[1])**2 + int(vec_B[2])**2)
total4 ='{0:0.2f}'.format(total4)
print("|B| =",total4)