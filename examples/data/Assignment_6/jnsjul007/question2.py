#Program to add, multply and obtain normalisation of vectors in strings
#Julian van Rensburg
#24 April 2014
#get empty string
import math
x=[]
#get inputs
A = input("Enter vector A:\n")
B = input("Enter vector B:\n")
#convert inputs to independant strings
a = A.split(' ')
b = B.split(' ')
#convert items in strings to integers, add to new empt strings respectively and add to empty string x
y = []
z = []
for item in a:
    
    y.append(int(item))
for item in b:
    z.append(int(item))

x.append(y)
x.append(z)
#print addition of correstponding elements

u=round(math.sqrt(x[0][0]**2 + x[0][1]**2+x[0][2]**2),2)
o=round(math.sqrt(x[1][0]**2 + x[1][1]**2+x[1][2]**2),2)

print ("A+B = ","[",x[0][0]+x[1][0],", ",x[0][1]+x[1][1],", ",x[0][2]+x[1][2],"]",sep='')
print("A.B =",x[0][0]*x[1][0]+x[0][1]*x[1][1]+x[0][2]*x[1][2])
print("|A| = {0:0.2f}".format(u)) #round(math.sqrt(x[0][0]**2 + x[0][1]**2+x[0][2]**2),2))
print("|B| = {0:0.2f}".format(o)) #round(math.sqrt(x[1][0]**2 + x[1][1]**2+x[1][2]**2),2))