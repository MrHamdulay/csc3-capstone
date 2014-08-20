def q2():
    import math
    a = []
    b = []
    vectorsA = input("Enter vector A:\n")
    listA = vectorsA.split(' ')
    vectorsB = input("Enter vector B:\n")
    listB = vectorsB.split(' ')
    
    for i in range(len(listA)):
        j = eval(listA[i]) + eval(listB[i])
        a.append(j)
    print('A+B = ',a,sep='')
    
    sumproduct = 0
    for k in range(len(listA)):
        product = eval(listA[k]) * eval(listB[k])
        sumproduct += product
        
    print("A.B = ",sumproduct,sep='')
    
    sumsquares = 0
    for i in range(len(listA)):
        square = (eval(listA[i]))**2
        sumsquares += square
    print("|A| = ", "{0:.2f}".format(round(math.sqrt(sumsquares),2)),sep='')
    
    sumsquares = 0
    for i in range(len(listB)):
        square = (eval(listB[i]))**2
        sumsquares += square
    print("|B| = ", "{0:.2f}".format(round(math.sqrt(sumsquares),2)),sep='')    
    
q2()
    