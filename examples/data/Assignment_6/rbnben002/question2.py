import math
userA = input(("Enter vector A:\n"))
listA = userA.split(" ")
userB = input(("Enter vector B:\n"))
listB = userB.split(" ")
Addition = [eval(listA[0]) + eval(listB[0]),eval(listA[1]) + eval(listB[1]),eval(listA[2]) + eval(listB[2])]
Sum = ((eval(listA[0])*eval(listB[0]))+(eval(listA[1])*eval(listB[1]))+(eval(listA[2])*eval(listB[2])))
NormA = round(math.sqrt(eval(listA[0])**2 + eval(listA[1])**2+ eval(listA[2])**2),2)
NormB = round(math.sqrt(eval(listB[0])**2+ eval(listB[1])**2+ eval(listB[2])**2),2)
print("A+B =",Addition)
print("A.B =",Sum)
print("|A| =","{0:.2f}".format(NormA))
print("|B| =","{0:.2f}".format(NormB))





    
