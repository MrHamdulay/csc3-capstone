import math

vecA = (input("Enter vector A:\n"))
vecB = (input("Enter vector B:\n"))

vecAn = vecA.split()
vecBn = vecB.split()

f = int(vecAn[0])
g = int(vecBn[0])
h = int(vecAn[1])
i = int(vecBn[1])
j = int(vecAn[2])
k = int(vecBn[2])

ab = [(f+g),(h+i),(j+k)]
abdot = (f*g)+(h*i)+(j*k)
amod = round(math.sqrt(f**2+h**2+j**2),2)
bmod = round(math.sqrt(g**2+i**2+k**2),2)

print("A+B =",ab)
print("A.B =",abdot)
print("|A| =","%0.2f" % (amod,))
print("|B| =","%0.2f" % (bmod,))
