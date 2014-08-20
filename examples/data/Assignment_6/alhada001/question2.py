import math
A = input("Enter vector A:\n").split(" ") #User enters first series of numbers
B = input("Enter vector B:\n").split(" ") #User enters second series of numbers
sum = [eval(A[0])+ eval(B[0]),eval(A[1])+ eval(B[1]),eval(A[2])+ eval(B[2])] #Each block is added with the corresponding block in the other vector
print("A+B =",sum) #Prints the resuls of calculation
times = eval(A[0]) * eval(B[0]) + eval(A[1]) * eval(B[1]) + eval(A[2]) * eval(B[2]) #The two vectors are multiplied by eachother
print("A.B =", times) #The resuls of calculation are printed
abA = round(math.sqrt(eval(A[0])**2 + eval(A[1])**2+ eval(A[2])**2),2)
abB = round(math.sqrt(eval(B[0])**2+ eval(B[1])**2+ eval(B[2])**2),2)
abA = "%.2f" % abA
abB = "%.2f" % abB
print("|A| =",abA)
print("|B| =",abB)