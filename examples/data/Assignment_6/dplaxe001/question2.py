'''Vector claculations program
Axel du Plessis
20-04-2014'''

form = '{0:0<4}'

vectorA = input("Enter vector A:\n").split(" ")
vectorB = input("Enter vector B:\n").split(" ")

sumVector = []
prodVector = 0
vectorSquaredSumA = 0
vectorSquaredSumB = 0

for i in range(3):
    sumVector.append(eval(vectorA[i])+eval(vectorB[i]))
    prodVector += eval(vectorA[i])*eval(vectorB[i])
    vectorSquaredSumA += eval(vectorA[i])**2
    vectorSquaredSumB += eval(vectorB[i])**2
    
print("A+B = "+str(sumVector))
print("A.B = "+str(prodVector))
print("|A| = "+str(form.format(round(vectorSquaredSumA**(1/2),2))))
print("|B| = "+str(form.format(round(vectorSquaredSumB**(1/2),2))))
