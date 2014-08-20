"""Program to do basic vector calculations in 3d
John Odetokun ODTJOH001
20 April 2014"""
#importing maths class
import math
#vector A
vectA = input("Enter vector A:\n").split(" ")
#vector B
vectB = input("Enter vector B:\n").split(" ")

vectApB = []
vectAmB = 0
absA = 0
absB = 0
for i in range(3):
    #vector addition
    vectApB.append(int(vectA[i])+int(vectB[i]))
    #vector multiplication
    vectAmB += int(vectA[i])*int(vectB[i])
    #norm of A
    absA +=int(vectA[i])**2
    #norm of B
    absB += int(vectB[i])**2
#norm of A(continued)
absA = "{0:.2f}".format(math.sqrt(absA))
#norm of B(Continued)
absB = "{0:.2f}".format(math.sqrt(absB))
#answers printed
print("A+B =", vectApB)
print("A.B =",vectAmB)
print("|A| =",absA)
print("|B| =", absB)