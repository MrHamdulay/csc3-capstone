from math import sqrt
vector_A = str(input("Enter vector A:\n"))
A = vector_A.split()
vector_B = str(input("Enter vector B:\n"))
B = vector_B.split()
print("A+B = [",int(A[0])+int(B[0]),", ",int(A[1])+int(B[1]),", ",int(A[2])+int(B[2]),"]",sep="")
print("A.B =",int(A[0])*int(B[0]) + int(A[1])*int(B[1]) + int(A[2])*int(B[2]))
print("|A| =",'{0:1.2f}'.format(sqrt(int(A[0])**2 + int(A[1])**2 + int(A[2])**2),2))
print("|B| =",'{0:1.2f}'.format(sqrt(int(B[0])**2 + int(B[1])**2 + int(B[2])**2),2))