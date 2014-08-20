import math#To use special functions
#Creating empty lists
listA = []
listB = []
listFinal1 = []
listFinal2 = []
listFinal3 = []
listFinal4 = []
#User input
vecA = input("Enter vector A:\n")
vecB = input("Enter vector B:\n")
listA = vecA.split()
listB = vecB.split()
#Function to add vectors
def add(listA, listB):           
    for i in range(len(listA)):
        newList= eval(listA[i])+eval(listB[i])
        listFinal1.append(newList)
    print("A+B =",listFinal1)

add( listA, listB)
#Function to do dot product
def dot_product(listA,listB):
    for i in range(len(listA)):
        newList= eval(listA[i]) * eval(listB[i])
        listFinal2.append(newList)
    x = 0
    for i in listFinal2:
        x+=i 
    print("A.B =",x)

dot_product( listA,listB)
#Function to get magnitude
def magnitude(listA, listB):
    for i in range(len(listA)):
        newList= (eval(listA[i]))**2
        listFinal3.append(newList)  
    x= 0
    for i in listFinal3:
            x+=i 
    z = "{:.2f}".format(math.sqrt(x))
    
    print("|A| =", z)
    
    for i in range(len(listB)):
        newList= (eval(listB[i]))**2
        listFinal4.append(newList)  
    x= 0
    for i in listFinal4:
            x+=i 
    z = "{:.2f}".format(math.sqrt(x))
    print("|B| =", z)    
    
magnitude(listA, listB)