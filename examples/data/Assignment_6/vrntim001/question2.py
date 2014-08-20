"""Vector calculator
Timothy Mostert
23.14.14"""
import math

numbersA = input("Enter vector A:\n")
vectorA = numbersA.split()
numbersB = input("Enter vector B:\n")
vectorB = numbersB.split()

addition_list = []
addition0 = int(vectorA[0]) + int(vectorB[0])
addition1 = int(vectorA[1]) + int(vectorB[1])
addition2 = int(vectorA[2]) + int(vectorB[2])
addition_list.append(addition0)
addition_list.append(addition1)
addition_list.append(addition2)
print("A+B =", addition_list)


dot0 = int(vectorA[0]) * int(vectorB[0])
dot1 = int(vectorA[1]) * int(vectorB[1])
dot2 = int(vectorA[2]) * int(vectorB[2])
dotfinal = dot0 + dot1 + dot2
print("A.B =", dotfinal)

A = math.sqrt((eval(vectorA[0])**2) + (eval(vectorA[1])**2) + (eval(vectorA[2])**2))
print("|A| =", "{0:0<4}".format(str(round(A,2))))
B = math.sqrt((eval(vectorB[0])**2) + (eval(vectorB[1])**2) + (eval(vectorB[2])**2))
print("|B| =", "{0:0<4}".format(str(round(B,2))))