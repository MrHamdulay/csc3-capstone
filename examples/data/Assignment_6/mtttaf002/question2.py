"""vector calculations using lists
tafara mtutu
20 april 2014"""
import math

def normalize(v):
    total = 0
    for i in range(3):
        total += (eval(v[i]))**2
    if round(math.sqrt(total), 2) == 0:
        return "0.00"
    else: return round(math.sqrt(total), 2)
        

result =[]
total = 0
#ask user for vectors
vectorA = input("Enter vector A:\n")
vectorB = input("Enter vector B:\n")
A = vectorA.split(" ")
B = vectorB.split(" ")

#adding the 2 vectors
for i in range (3):
    result.append(eval(A[i]) + eval(B[i]))
print("A+B =",result)

#multiplying the two vectors
for i in range (3):
    total += eval(A[i]) * eval(B[i])
print("A.B =",total)

#normalizing vectors
print("|A| =", normalize(A))
print("|B| =", normalize(B))


