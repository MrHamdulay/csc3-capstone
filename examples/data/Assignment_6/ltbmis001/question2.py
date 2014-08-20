import math

A=input("Enter vector A:\n")
B=input("Enter vector B:\n")

listA = A.split(" ")
listB = B.split(" ")

list_sum = [eval(listA[0])+eval(listB[0]),(eval(listA[1])+eval(listB[1])),(eval(listA[2])+eval(listB[2]))]
print("A+B =",list_sum)

product = eval(listA[0])*eval(listB[0])+eval(listA[1])*eval(listB[1])+eval(listA[2])*eval(listB[2])
print("A.B = "+str(product))

sqrta = math.sqrt(eval(listA[0])*eval(listA[0])+eval(listA[1])*eval(listA[1])+eval(listA[2])*eval(listA[2]))
sqrtb = math.sqrt(eval(listB[0])*eval(listB[0])+eval(listB[1])*eval(listB[1])+eval(listB[2])*eval(listB[2]))

print("|A| = "+str("{0:.2f}".format(round(sqrta,2))))
print("|B| = "+str("{0:.2f}".format(round(sqrtb,2))))