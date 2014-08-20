#Addition, dot product and normalization of vectors
#Jennifer Yuan (YNXYIS001)
#22 April 2014

A = input("Enter vector A:\n") #obtain values for vector A from user
B = input("Enter vector B:\n") #obtain values for vector B from user

la = A.split(" ") #separate item into list of string
lb = B.split(" ")

x=0
for i in la: #converts string to numbers to do arithmetic
    y = eval(i) 
    la[x] = y #replacing strings with number equivalents
    x=x+1 #accumulator variable
x=0
for i in lb: #same as above, but for list lb
    y = eval(i)
    lb[x] = y
    x=x+1

print("A+B =", end = " ")
add = [] #empty string
x=0
while x<3:
    add.append(la[x] + lb[x]) #adds repsective values from la and lb to form new item in list add
    x = x+1 #accumulator variable 
print(add)

print("A.B =", end = " ")
dot = 0
x = 0
while x<3:
    y = la[x]*lb[x] #multiples repectives values from la and lb 
    dot = dot +y #accumulates all the answers 
    x=x+1 #accumulator variable 
print(dot)

print("|A| =", end = " ")
import math #to use functions within math library
square = 0
for i in la:
    y = i*i #squaring each value in list
    square = square+y #summing all squares as one value
root = math.sqrt(square) #taking square root of the some of all squares
if root != 0:
    print(round(root,2)) #rounds off answer to two decimal places
else:
    print("0.00")

print("|B| =", end = " ") #same as above, but for list lb
square = 0
for i in lb:
    y = i*i
    square = square+y
root = math.sqrt(square)
if root != 0:
    print(round(root,2)) #rounds off answer to two decimal places
else:
    print("0.00")