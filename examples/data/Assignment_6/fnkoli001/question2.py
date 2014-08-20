from math import sqrt

inpA = input("Enter vector A:\n")
inpB = input("Enter vector B:\n")

vecA = [eval(i) for i in inpA.split(" ")]
vecB = [eval(i) for i in inpB.split(" ")]

print("A+B =", [vecA[i] + vecB[i] for i in range(len(vecA))])
print("A.B =", sum([vecA[i] * vecB[i] for i in range(len(vecA))]))
if sum(vecA) == 0 and sum(vecB) == 0:
    print("|A| = 0.00")
    print("|B| = 0.00")
else:
    print("|A| =", round(sqrt(sum([vecA[i] ** 2 for i in range(len(vecA))])), 2))
    print("|B| =", round(sqrt(sum([vecB[i] ** 2 for i in range(len(vecB))])), 2))