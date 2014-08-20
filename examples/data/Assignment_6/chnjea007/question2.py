# assignment 6 question 2
import math
vectorA = input("Enter vector A:\n").split()
vectorB = input("Enter vector B:\n").split()
calc1 = []
calc2 = 0
calc3 = 0
calc4 = 0
for i in range (3):
    a = eval(vectorA[i])
    b = eval(vectorB[i])
    calc1.append(a + b)
    calc2 += a * b
    calc3 += a**2
    calc4 += b**2
calc3 = "{:.2f}".format(math.sqrt(calc3))
calc4 = "{:.2f}".format(math.sqrt(calc4))

print("A+B = ", calc1, sep = "")
print("A.B = ", calc2, sep = "")
print("|A| = ", calc3, sep = "")
print("|B| = ", calc4, sep = "")