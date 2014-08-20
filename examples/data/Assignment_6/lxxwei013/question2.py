"""Program to form basic vector calculations
Michelle Lu
19 April 2014"""
import math

#create lists
x=[]
y=[]
z=[]

#enter vectors
vA=input("Enter vector A:\n")
vA=vA.split(" ")
vB=input("Enter vector B:\n")
vB=vB.split(" ")

#store vectors in list
x.append(eval(vA[0])) #change them into integers
y.append(eval(vA[1]))
z.append(eval(vA[2]))
x.append(eval(vB[0]))
y.append(eval(vB[1]))
z.append(eval(vB[2]))

#add vectors
add=[]
add.append(x[0]+x[1])
add.append(y[0]+y[1])
add.append(z[0]+z[1])
print("A+B =", add)

#multiply vectors
dot=x[0]*x[1]+y[0]*y[1]+z[0]*z[1]
print("A.B =", dot)

#find magnitude of each vector
magA=math.sqrt(x[0]**2 + y[0]**2 + z[0]**2)
#magA=round(magA,2)
print("|A| =", "{:.2f}".format(magA))
magB=math.sqrt(x[1]**2 + y[1]**2+ z[1]**2)
#magB=round(magB,2)
print("|B| =", "{:.2f}".format(magB))
