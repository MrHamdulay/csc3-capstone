#program to do vector calculations
#michael field
#21 april 2014

#calc sum of vectors
def calcVecSum(a,b):
    vecSum = []
    for i in range(3):
        vecSum.append(eval(a[i]) + eval(b[i]))
    
    return vecSum

#calc dot product
def calcDotPro(a,b):
    dotPro = []
    
    #calc product of each vector
    for i in range(3):
        dotPro.append(eval(a[i])*eval(b[i]))
    
    #calc sum
    sum1 = 0
    for j in range(3):
        sum1 += dotPro[j]
    
    return sum1

#calc normal function
def calcNorm(num):
    norm = 0
    vSquared = []
    sumSquares = 0
    
    #square each vector
    for i in range(3):
        vSquared.append(eval(num[i])**2)
    
    #calc sum of squares
    for j in range(3):
        sumSquares += vSquared[j]
        
    #calc norm and round off
    norm = sumSquares ** 0.5
    norm = round(norm,2)
    
    if norm == 0.0:
        return "0.00"
    else:
        return norm

#get vectors
a = []
b = []
    
a_in = input("Enter vector A:\n")
b_in = input("Enter vector B:\n")

a = a_in.split()
b = b_in.split()

#output vector sum
Vsum = calcVecSum(a,b)
print("A+B =", Vsum)

#output dot product
dotPro = calcDotPro(a,b)
print("A.B =", dotPro)

#output norm
normA = calcNorm(a)
normB = calcNorm(b)
print("|A| =", normA)
print("|B| =", normB)