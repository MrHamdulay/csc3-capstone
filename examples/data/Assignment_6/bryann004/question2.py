#Anna Borysova
#ass6,q2
#2014-04-22
import math
A = input("Enter vector A:\n").split(" ")
B = input("Enter vector B:\n").split(" ")
add_AB = []
dot_AB = 0
norm_A = 0
norm_B = 0
for i in range(3):
    A[i] = int(A[i])
    B[i] = int(B[i])
    add_AB.append(A[i]+B[i])
    dot_AB += A[i]*B[i]
    norm_A += (A[i]**2)
    norm_B += (B[i]**2)

print("A+B =", add_AB)
print("A.B =", dot_AB)
print("|A| =", "{:0.2f}".format(round(math.sqrt(norm_A), 2))) # format output
print("|B| =", "{:0.2f}".format(round(math.sqrt(norm_B), 2)))