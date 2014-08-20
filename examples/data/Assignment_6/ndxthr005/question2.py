"""thrianka naidoo
ndxthr005
assignment 6: question 2, a program to manipulate data using mathematical operators """

vecA = input("Enter vector A: \n")      #input for user
vecB = input("Enter vector B: \n")

listA = vecA.split(" ")                 #spliting string into list 
listB = vecB.split(" ")
#print(listA)
#print(listB)

listA1 = int(listA[0])                  #divides listA into 3 values
listA2 = int(listA[1])
listA3 = int(listA[2])

listB1 = int(listB[0])                  #divides listB into 3 values
listB2 = int(listB[1])
listB3 = int(listB[2])

#addition
add1 = listA1 + listB1
add2 = listA2 + listB2
add3 = listA3 + listB3
listAdd = [add1,add2,add3]
print("A+B","=",listAdd)

#dot multiplication
mult1 = listA1 * listB1
mult2 = listA2 * listB2
mult3 = listA3 * listB3
totMult = mult1+mult2+mult3
print("A.B","=",totMult)

#square A
import math

sqrtListA = round(math.sqrt((listA1**2 + listA2**2 + listA3**2)),2)
print("|A| = %.2f"%(sqrtListA))

#square B
sqrtListB = round(math.sqrt((listB1**2 + listB2**2 + listB3**2)),2)
print("|B| = %.2f"%sqrtListB)