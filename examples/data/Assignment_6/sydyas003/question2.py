import math#Import mathematics library for square root function

#Input both vectors
a=input("Enter vector A:\n")
b=input("Enter vector B:\n")

#Split both vectors into lists
A=a.split()
B=b.split()

sum_list=[ ]#List to store sums
product=0#Initialise product variable
#Initialise absolute variables
a_absolute=0 
b_absolute=0 

#for loop to run through lists and calculate sum, product and absolute
for num in range(len(A)):
    A[num]=eval(A[num])
    B[num]=eval(B[num])
    sum_list.append(A[num]+B[num])
    product+=A[num]*B[num]
    a_absolute+=(A[num])**2
    b_absolute+=(B[num])**2

#Calculate and format absolute values
a_absolute=math.sqrt(a_absolute)
a_absolute="{0:.2f}".format(a_absolute)

b_absolute=math.sqrt(b_absolute)
b_absolute="{0:.2f}".format(b_absolute)

#Print final output
print ("A+B =",sum_list)
print ("A.B =",product)
print("|A| =",a_absolute)
print("|B| =",b_absolute)