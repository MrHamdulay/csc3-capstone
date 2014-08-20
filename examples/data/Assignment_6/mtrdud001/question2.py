"""Matrices, adding multiplying, squaring
Dudley Mutero
14/4/24"""

import math

list1=[]
list2=[]
addlist=[]
productanswer=0
sqrtA=0
sqrtB=0         #all are global variables either to be updated by functions or contain data to be used by functions

def multiply(): #this function multiplies the vectors given
    a=eval(list1[0])*eval(list2[0])
    b=eval(list1[1])*eval(list2[1])
    c=eval(list1[2])*eval(list2[2])
    productanswer=a+b+c
    print ("A.B =",round(productanswer,2))
  
    
def add(): #adding two vectors and storing in global variable list
    d=eval(list1[0])+eval(list2[0])
    addlist.append(d)
    e=eval(list1[1])+eval(list2[1]) 
    addlist.append(e)
    f=eval(list1[2])+eval(list2[2]) 
    addlist.append(f)
    
def sqrt1():#squareroot of vector a and storing in global variable sqrt
    f=eval( list2[0])**2+ eval(list2[1])**2 + eval(list2[2])**2
    sqrtB=math.sqrt(f)
    print ("|B| =","{0:.2f}".format(sqrtB))

def sqrt2(): #squareroot of vector a and storing in global variable sqrt
    g= eval(list1[0])**2+ eval(list1[1])**2 + eval(list1[2])**2
    sqrtA=math.sqrt(g)
    print ("|A| =","{0:.2f}".format(sqrtA))
    

i=input ("Enter vector A:\n")#ask user for vector 1
list1=i.split()
j=input("Enter vector B:\n")#ask user for vector 2
list2=j.split()
add()
print ("A+B =",addlist)
multiply()
sqrt2()
sqrt1() #invoking the functions to work befor
