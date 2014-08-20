import math

vectora = (input("Enter vector A:\n")).split()
vectorb = (input("Enter vector B:\n")).split()
added = [0,0,0]
for i in range(3):
    vectora[i] = int(vectora[i])
    vectorb[i] = int(vectorb[i])
    added[i] = vectora[i] + vectorb[i]
print("A+B = "+str(added))

totalprod = 0
for j in range(3):
    totalprod += vectora[j]*vectorb[j]
print("A.B = " + str(totalprod))


TotSqrA = ((vectora[0])*(vectora[0]))+((vectora[1])*(vectora[1]))+((vectora[2])*(vectora[2]))
TotSqrB = ((vectorb[0])*(vectorb[0]))+((vectorb[1])*(vectorb[1]))+((vectorb[2])*(vectorb[2]))    

print("|A| = " + "{0:.2f}".format(math.sqrt(TotSqrA)))
print("|B| = " + "{0:.2f}".format(math.sqrt(TotSqrB)))