import math

VA = input("Enter vector A:\n")
A = VA.split(" ")

VB = input("Enter vector B:\n")
B = VB.split(" ")

step2A = []
for i in range(len(A)):
    step1A = eval(A[i]) + eval(B[i])
    step2A.append(step1A)  
print("A+B = ", step2A, sep="")

step2B = 0
for j in range(len(A)):
    step1B = eval(A[j])*eval(B[j])
    step2B += step1B
print("A.B = ", step2B, sep ="")

step2C = 0
for l in range(len(A)):
    step1C = eval(A[l])**2
    step2C += step1C
    
step3C = math.sqrt(step2C)

step3C = str(step3C)
step3Cwee = step3C.split(".")
step3C2 = step3Cwee[1][0:2]


if eval(step3C2) != 0:
    step3C2 = round(eval(step3C),2)
    print("|A| = " + str(step3C2))
    
else:
    form = "{0:0<2}"
    print("|A| = " + step3Cwee[0] + "." + form.format(step3C2))

step2D = 0
for k in range(len(B)):
    step1D = eval(B[k])**2
    step2D += step1D
    
step3D = math.sqrt(step2D)

step3D = str(step3D)
step3Dwee = step3D.split(".")
step3D2 = step3Dwee[1][0:2]

if eval(step3D2) != 0:
    step3D2 = round(eval(step3D),2)
    print("|B| = " + str(step3D2))
    
else:
    form = "{0:0<2}"
    print("|B| = " + step3Dwee[0] + "." + form.format(step3D2))
