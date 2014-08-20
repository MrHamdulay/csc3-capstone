#Assignment 6 Question 2
#19 April 2014
#Alexi Kalamoudacos, Vector Calculations

import math

def VectorAddition(a,b):
#Add the indexed numbers together to form a new index of added numbers
    VecSum=[a[0]+b[0], a[1]+b[1], a[2]+b[2]]
    return VecSum

def VectorMultiplication(a,b):
#Multiply the indexed numbers and add to return multiplied vector
    VecMult=a[0]*b[0]+a[1]*b[1]+a[2]*b[2]
    return VecMult

def VectorAbsolute(a):
#Calculate the absolute value of the vector then round to 2 decimal places
    VecAbs=math.sqrt((a[0]**2)+(a[1]**2)+(a[2]**2))
    VecAbs="{:.2f}".format(VecAbs)
    return VecAbs

Vec1Input=input('Enter vector A:\n')
Vec2Input=input('Enter vector B:\n')

Vec1=[]
Vec2=[]
#Get the string values of each number separated
StringVec1=Vec1Input.split(' ')
#Evaluate the strings to form numbers, then add those numbers to a new list
for i in StringVec1:
    x=eval(i)
    Vec1.append(x)

StringVec2=Vec2Input.split(' ')
for i in StringVec2:
    x=eval(i)
    Vec2.append(x)

print('A+B =',VectorAddition(Vec1,Vec2))
print('A.B =',VectorMultiplication(Vec1,Vec2))
print('|A| =',VectorAbsolute(Vec1))
print('|B| =',VectorAbsolute(Vec2))